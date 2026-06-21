from itertools import groupby

def rle_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    for char, group in groupby(input_string):
        count = sum(1 for _ in group)
        if count > 1:
            result.append(f"{count}{char}")
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    encoded_output = rle_encode(sample_input)
    print(encoded_output)