import argparse
import re

def read_text(filename: str) -> str:
    """ function for read from file """
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found")
        exit(2)
    except PermissionError:
        print(f"Premision denied")
        exit(2)
    except Exception as e:
        print(e)
        exit(2)

def staticstic(text: str) -> dict:
    word_set = set(text)
    dictionary = {i:0 for i in word_set}
    for word in text:
            dictionary[word] += 1
    for i,j in dictionary.items():
         dictionary[i] = j/len(text)
    sorted_dictonary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dictonary

def decode(text:str, key:dict) -> str: 
    """
    Decoding text
    """
    for i, j in key.items():
        text = text.replace(i, j)
    return text    

def str_to_dict(str: str) -> dict:
    str = str.split("\n")
    dict_str={}
    for k in str:
        buf = re.split(r"[\n\t,;]", k)
        dict_str[buf[0]]=buf[1]
    return dict_str

def terminal_parsing():
    parser = argparse.ArgumentParser(description='Polibius encode')
    parser.add_argument('--input_file', required=True, help='file with text')
    parser.add_argument('--key', required=True, help='key for encode')
    parser.add_argument('--output_file', required=True, help='file for encode text')
    parser.add_argument('--statistic_file', required=True, help='file for encode text')
    args = parser.parse_args()
    return args

def write_staticstic(filename: str, statistic: dict) -> None:
     try:
        with open("statistic.txt", "w", encoding="utf-8") as f:
               for i,j in statistic.items():
                      f.write(i + "\t" + str(j) + "\n")
     except PermissionError:
        print(f"Permission denied")
        exit(2)
     except Exception as e:
        print(e)
        exit(2)
    
def write_text(filename: str, text: str) -> str:
    """ function for write to file """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)    
    except PermissionError:
        print(f"Permission denied")
        exit(2)
    except Exception as e:
        print(e)
        exit(2)   

def main() -> None:
    args = terminal_parsing()
    text = read_text(args.input_file)
    stat = staticstic(text)
    write_staticstic(args.statistic_file,stat)
    key = read_text(args.key)
    key = str_to_dict(key)
    answer = decode(text, key)
    write_text(args.output_file , answer)
    print("program end")


if __name__ == "__main__":
     main()
        