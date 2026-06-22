import re

class RLEDecoder:
    def __init__(self):
        self.pattern = re.compile(r'(\d+)|(\D)')

    def decode(self, encoded_string):
        if not isinstance(encoded_string, str):
            raise ValueError("Input must be a string")
        
        result = []
        pos = 0
        length = len(encoded_string)
        
        while pos < length:
            if encoded_string[pos].isdigit():
                count_start = pos
                while pos < length and encoded_string[pos].isdigit():
                    pos += 1
                count = int(encoded_string[count_start:pos])
                
                if pos >= length:
                    raise ValueError(f"Invalid RLE format: count '{count}' has no character following it")
                
                char = encoded_string[pos]
                result.append(char * count)
                pos += 1
            else:
                char = encoded_string[pos]
                result.append(char)
                pos += 1
        
        return ''.join(result)

if __name__ == '__main__':
    decoder = RLEDecoder()
    test_cases = [
        "12a3b",
        "2x5y1z",
        "a3b2c",
        "100z",
        "7",
        "123"
    ]
    
    for test in test_cases:
        try:
            output = decoder.decode(test)
            print(f"Input: {test} -> Output: {output}")
        except ValueError as e:
            print(f"Input: {test} -> Error: {e}")
    
    invalid_case = "12a3"
    try:
        decoder.decode(invalid_case)
    except ValueError as e:
        print(f"Input: {invalid_case} -> Error: {e}")