def run_length_encode(text):
    if not text:
        return {}
    
    encoded_dict = {}
    current_char = text[0]
    current_count = 1
    
    for char in text[1:]:
        if char.isalnum() and char == current_char:
            current_count += 1
        else:
            if char.isalnum():
                encoded_dict[current_char] = current_count
                current_char = char
                current_count = 1
            else:
                current_char = char
                current_count = 1
    
    if current_char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        encoded_dict[current_char] = current_count
    
    return encoded_dict

if __name__ == '__main__':
    result = run_length_encode("AAABBC")
    print(result)