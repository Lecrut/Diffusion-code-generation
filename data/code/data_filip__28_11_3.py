def run_length_encode(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    compressed = []
    count = 1
    current_char = binary_string[0]
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = binary_string[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    
    return "".join(compressed)

if __name__ == '__main__':
    sample1 = "1100011110"
    sample2 = "1"
    sample3 = ""
    sample4 = "0000"
    
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))