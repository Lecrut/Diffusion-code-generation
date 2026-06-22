import itertools
import sys

def run_length_encode(data):
    if not data:
        return ""
    
    chunks = []
    
    for char, group in itertools.groupby(data):
        count = len(list(group))
        chunks.append(str(count))
        chunks.append(char)
    
    return "".join(chunks)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    result = run_length_encode(sample_string)
    print(result)