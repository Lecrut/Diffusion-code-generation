from itertools import groupby

def run_length_encode(text):
    if not text:
        return ""
    
    encoded_groups = []
    
    for key, group in groupby(text):
        count = sum(1 for _ in group)
        encoded_groups.append(f"{count}{key}")
        
    return "".join(encoded_groups)

if __name__ == '__main__':
    input_string = "aaabbcdd"
    result = run_length_encode(input_string)
    print(result)