from typing import Union

def trim_whitespace(text: Union[str, None]) -> Union[str, None]:
    if text is None:
        return None
    return text.strip()

if __name__ == '__main__':
    sample1 = "   Hello World   "
    sample2 = "\t\tPython Code\n\n"
    sample3 = None
    
    result1 = trim_whitespace(sample1)
    result2 = trim_whitespace(sample2)
    result3 = trim_whitespace(sample3)
    
    print(result1)
    print(result2)
    print(result3)