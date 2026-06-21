class RLEEncoder:
    def encode(self, input_string):
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string")
        
        if not input_string:
            return []
        
        result = []
        current_char = input_string[0]
        count = 1
        
        for i in range(1, len(input_string)):
            char = input_string[i]
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    result = encoder.encode("AAABBC")
    print(result)
    
    result_empty = encoder.encode("")
    print(result_empty)
    
    result_single = encoder.encode("Z")
    print(result_single)