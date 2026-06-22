def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = input_string[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_strings = [
        "AABCCC",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB",
        "",
        "A",
        "ABC",
        "AAABBBCCC"
    ]
    
    for s in sample_strings:
        print(run_length_encode(s))