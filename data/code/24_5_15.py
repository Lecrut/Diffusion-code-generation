def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    encoded = []
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(f"{data[i - 1]}{count}")
            count = 1
    
    encoded.append(f"{data[-1]}{count}")
    return "".join(encoded)

def run_length_decode(encoded: str) -> str:
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num_str = ""
        
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        count = int(num_str)
        decoded.append(char * count)
    
    return "".join(decoded)

if __name__ == '__main__':
    test_string = "AAAABBBCCDAAA"
    encoded_result = run_length_encode(test_string)
    print(encoded_result)
    
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)