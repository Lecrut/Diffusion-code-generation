def run_length_encode(text):
    if not text:
        return ""
    
    encoded_parts = []
    scan_index = 0
    total_length = len(text)
    
    while scan_index < total_length:
        target_char = text[scan_index]
        run_count = 0
        check_index = scan_index
        
        while check_index < total_length and text[check_index] == target_char:
            run_count += 1
            check_index += 1
        
        encoded_parts.append(target_char + str(run_count))
        scan_index = check_index
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    input_data = 'xxxyyyzzzwwwww'
    output_data = run_length_encode(input_data)
    print(output_data)