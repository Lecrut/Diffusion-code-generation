def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "aaabbcccc"
    result = run_length_encode(sample_text)
    print(result)