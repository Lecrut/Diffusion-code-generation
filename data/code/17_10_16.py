import itertools

def run_length_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    
    for key, group in itertools.groupby(input_string):
        count = len(list(group))
        if count > 1:
            result.append(f"{count}{key}")
        else:
            result.append(key)
            
    return "".join(result)

if __name__ == '__main__':
    sample = "aabcccccaaa"
    encoded = run_length_encode(sample)
    print(encoded)