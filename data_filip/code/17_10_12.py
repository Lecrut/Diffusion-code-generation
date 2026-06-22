def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    iterator = iter(s)
    prev_char = next(iterator)
    count = 1
    
    for char in iterator:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = char
            count = 1
    
    result.append(f"{count}{prev_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbc"
    encoded = run_length_encode(sample_string)
    print(encoded)