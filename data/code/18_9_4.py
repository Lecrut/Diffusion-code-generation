def run_length_encode(data):
    if not data:
        return ""
    
    result = []
    length = len(data)
    i = 0
    
    while i < length:
        current_char = data[i]
        count = 1
        
        while i + 1 < length and data[i + 1] == current_char:
            count += 1
            i += 1
        
        result.append(str(count))
        result.append(current_char)
        i += 1
    
    return "".join(result)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)