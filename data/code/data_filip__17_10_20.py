from itertools import groupby

def run_length_encode(s):
    if not s:
        return ""
    
    encoded_parts = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        if count == 1:
            encoded_parts.append(char)
        else:
            encoded_parts.append(f"{count}{char}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    input_string = "aaabbc"
    result = run_length_encode(input_string)
    print(result)