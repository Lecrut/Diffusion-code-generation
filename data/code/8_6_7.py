import re

def split_comma_string(s: str) -> list:
    return [x.strip() for x in re.split(r',\s*', s) if x.strip()]

if __name__ == '__main__':
    sample_input = "  hello , world , foo ,  bar , "
    result = split_comma_string(sample_input)
    print(result)