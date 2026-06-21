def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = data[i]
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbbcccccaad"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    empty_string = ""
    print(run_length_encode(empty_string))
    single_char = "z"
    print(run_length_encode(single_char))