class RLEDecoder:
    def __init__(self, encoded_string):
        self.encoded_string = encoded_string
    
    def decode(self):
        if not self.encoded_string:
            return ""
        
        result = []
        i = 0
        n = len(self.encoded_string)
        
        while i < n:
            if not self.encoded_string[i].isdigit():
                raise ValueError(f"Invalid input format: expected digit at index {i}, got '{self.encoded_string[i]}'")
            
            count_start = i
            while i < n and self.encoded_string[i].isdigit():
                i += 1
            
            count_str = self.encoded_string[count_start:i]
            count = int(count_str)
            
            if i >= n:
                raise ValueError("Invalid input format: missing character after count")
            
            char = self.encoded_string[i]
            i += 1
            
            if count < 0:
                raise ValueError(f"Invalid count value: {count} at position {count_start}")
            
            result.append(char * count)
        
        return "".join(result)

if __name__ == '__main__':
    sample1 = "3A5B2C"
    decoder1 = RLEDecoder(sample1)
    print(decoder1.decode())
    
    sample2 = "10X2Y3Z"
    decoder2 = RLEDecoder(sample2)
    print(decoder2.decode())
    
    sample3 = "123a1b"
    decoder3 = RLEDecoder(sample3)
    print(decoder3.decode())