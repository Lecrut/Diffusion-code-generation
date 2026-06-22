class RLEProcessor:
    def __init__(self, delimiter=''):
        self._delimiter = delimiter

    def encode(self, text):
        if not text:
            return ""
        
        length = len(text)
        if length == 1:
            return "1" + text
        
        result = []
        current_char = text[0]
        current_count = 1
        
        for i in range(1, length):
            char = text[i]
            if char == current_char:
                current_count += 1
            else:
                result.append(str(current_count))
                result.append(current_char)
                result.append(self._delimiter)
                current_char = char
                current_count = 1
        
        result.append(str(current_count))
        result.append(current_char)
        
        return "".join(result)

if __name__ == '__main__':
    processor = RLEProcessor(delimiter='')
    
    sample_a = "AAABBBCCD"
    encoded_a = processor.encode(sample_a)
    print(encoded_a)
    
    sample_b = "A"
    encoded_b = processor.encode(sample_b)
    print(encoded_b)
    
    sample_c = ""
    encoded_c = processor.encode(sample_c)
    print(encoded_c)
    
    sample_d = "XYZ"
    encoded_d = processor.encode(sample_d)
    print(encoded_d)