import re

def escape_rle_encode(data):
    if not data:
        return ''
    
    ESCAPE = '\x1B'
    RUN_LENGTH = 3
    encoded = []
    
    i = 0
    while i < len(data):
        char = data[i]
        
        if char == ESCAPE:
            encoded.append(ESCAPE)
            encoded.append(ESCAPE)
            i += 1
            continue
        
        if char.isdigit():
            count = 1
            while i + count < len(data) and data[i + count] == char and count < 999:
                count += 1
            
            if count > RUN_LENGTH:
                encoded.append(ESCAPE)
                encoded.append(str(count).zfill(3))
                encoded.append(char)
                i += count
            else:
                for _ in range(count):
                    encoded.append(char)
                i += count
        else:
            count = 1
            while i + count < len(data) and data[i + count] == char and count < 999:
                count += 1
            
            if count > RUN_LENGTH:
                encoded.append(ESCAPE)
                encoded.append(str(count).zfill(3))
                encoded.append(char)
                i += count
            else:
                for _ in range(count):
                    encoded.append(char)
                i += count
    
    return ''.join(encoded)

def escape_rle_decode(encoded_data):
    if not encoded_data:
        return ''
    
    ESCAPE = '\x1B'
    decoded = []
    
    i = 0
    while i < len(encoded_data):
        char = encoded_data[i]
        
        if char == ESCAPE:
            if i + 1 < len(encoded_data) and encoded_data[i + 1] == ESCAPE:
                decoded.append(ESCAPE)
                i += 2
                continue
            
            if i + 4 < len(encoded_data):
                count_str = encoded_data[i + 1:i + 4]
                if count_str.isdigit():
                    count = int(count_str)
                    next_char = encoded_data[i + 4]
                    decoded.append(next_char * count)
                    i += 5
                    continue
            
            decoded.append(char)
            i += 1
            continue
        
        decoded.append(char)
        i += 1
    
    return ''.join(decoded)

if __name__ == '__main__':
    original1 = "Hello World"
    encoded1 = escape_rle_encode(original1)
    decoded1 = escape_rle_decode(encoded1)
    print(decoded1)
    
    original2 = "AAAAAAABBBBB"
    encoded2 = escape_rle_encode(original2)
    decoded2 = escape_rle_decode(encoded2)
    print(decoded2)
    
    original3 = "A\x1BB"
    encoded3 = escape_rle_encode(original3)
    decoded3 = escape_rle_decode(encoded3)
    print(decoded3)
    
    original4 = "123123123"
    encoded4 = escape_rle_encode(original4)
    decoded4 = escape_rle_decode(encoded4)
    print(decoded4)
    
    original5 = ""
    encoded5 = escape_rle_encode(original5)
    decoded5 = escape_rle_decode(encoded5)
    print(decoded5)