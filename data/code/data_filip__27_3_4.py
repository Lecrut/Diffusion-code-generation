import json
import copy

class RLEEncoder:
    def __init__(self, input_string):
        self.input_string = input_string
        self.encoded_data = []

    def encode(self):
        if not self.input_string:
            return []
        
        encoded = []
        length = len(self.input_string)
        index = 0
        
        while index < length:
            current_char = self.input_string[index]
            count = 1
            
            while (index + count < length) and (self.input_string[index + count] == current_char):
                count += 1
            
            encoded.append(current_char)
            encoded.append(count)
            index += count
            
        self.encoded_data = encoded
        return self.encoded_data

    def get_json_result(self):
        return json.dumps(self.encoded_data)

if __name__ == '__main__':
    sample_string = "aabcccccaaa"
    
    encoder = RLEEncoder(sample_string)
    result = encoder.encode()
    
    print(result)
    print(encoder.get_json_result())