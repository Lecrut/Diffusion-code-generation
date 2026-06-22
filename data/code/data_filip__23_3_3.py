import itertools

def run_length_encode(text):
    if not text:
        return ""
    
    groups = itertools.groupby(text)
    encoded_parts = []
    
    for char, group in groups:
        count = sum(1 for _ in group)
        encoded_parts.append(f"{count}{char}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample1 = "AAABBBCCCDAA"
    sample2 = "ABCDE"
    sample3 = ""
    sample4 = "A"
    sample5 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))