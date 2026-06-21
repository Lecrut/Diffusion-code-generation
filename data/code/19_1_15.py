import re

def decode_rle(encoded_string):
    if not encoded_string:
        return ""
    
    pattern = re.compile(r'(\d+)([A-Za-z])|([A-Za-z])')
    result = []
    
    i = 0
    n = len(encoded_string)
    
    while i < n:
        if encoded_string[i].isdigit():
            num_start = i
            while i < n and encoded_string[i].isdigit():
                i += 1
            count = int(encoded_string[num_start:i])
            if i < n:
                char = encoded_string[i]
                if char.isalpha():
                    result.append(char * count)
                    i += 1
                else:
                    raise ValueError(f"Invalid character '{char}' after count")
            else:
                raise ValueError("Incomplete encoding: count without following character")
        elif encoded_string[i].isalpha():
            result.append(encoded_string[i])
            i += 1
        else:
            raise ValueError(f"Invalid character '{encoded_string[i]}'")
    
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        "2A3B",
        "10C",
        "A2B",
        "3A2B4C",
        "1X2Y3Z",
        "",
        "5A",
        "A1B",
    ]
    
    for sample in sample_inputs:
        try:
            decoded = decode_rle(sample)
            print(decoded)
        except Exception as e:
            print(f"Error: {e}")