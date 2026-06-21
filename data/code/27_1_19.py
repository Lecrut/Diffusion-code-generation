def run_length_encode(data):
    if not data:
        return []
    
    encoded_data = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded_data.append((current_char, count))
            current_char = data[i]
            count = 1
            
    encoded_data.append((current_char, count))
    return encoded_data

if __name__ == '__main__':
    sample_string = 'AAAABBBCCDAA'
    result = run_length_encode(sample_string)
    print(result)