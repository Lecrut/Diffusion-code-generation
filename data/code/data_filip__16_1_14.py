import json

def run_length_encode(input_list):
    if not input_list:
        return []
    
    encoded = []
    current_value = input_list[0]
    count = 1
    
    for i in range(1, len(input_list)):
        value = input_list[i]
        if value == current_value:
            count += 1
        else:
            encoded.append([current_value, count])
            current_value = value
            count = 1
    
    encoded.append([current_value, count])
    return encoded

def run_length_decode(encoded_list):
    decoded = []
    for item in encoded_list:
        value, count = item
        decoded.extend([value] * count)
    return decoded

if __name__ == '__main__':
    original = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    encoded_result = run_length_encode(original)
    decoded_result = run_length_decode(encoded_result)
    
    print(encoded_result)
    print(decoded_result)