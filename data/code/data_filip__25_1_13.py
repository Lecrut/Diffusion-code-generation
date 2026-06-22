import re

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    def replace_match(match):
        char = match.group(1)
        length = len(match.group(0))
        if length > 1:
            return f"{length}{char}"
        return char

    pattern = r"(.)(\1*)"
    return re.sub(pattern, replace_match, s)

if __name__ == '__main__':
    input_str = "aaabbbccc"
    result = compress_string(input_str)
    print(result)