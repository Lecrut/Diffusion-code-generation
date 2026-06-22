def run_length_encode(data):
    if not data:
        return ''
    
    encoded = []
    count = 1
    length = len(data)
    
    for index in range(length):
        if index + 1 < length and data[index] == data[index + 1]:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(data[index])
            count = 1
    
    return ''.join(encoded)

if __name__ == '__main__':
    sample_input = 'aaabbbccca'
    result = run_length_encode(sample_input)
    print(result)
    
    empty_input = ''
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    single_char = 'z'
    single_result = run_length_encode(single_char)
    print(single_result)