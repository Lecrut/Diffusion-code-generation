import json

class RLEncoder:
    def __init__(self):
        self.sample_string = "AAABBBCCCCDDDDEEEEE"

    def encode(self, input_string=None):
        if input_string is None:
            input_string = self.sample_string
        
        if not input_string:
            return []
        
        result = []
        index = 0
        total_length = len(input_string)
        
        while index < total_length:
            current_char = input_string[index]
            count = 0
            while index < total_length and input_string[index] == current_char:
                count += 1
                index += 1
            result.append([current_char, count])
        
        return result

if __name__ == '__main__':
    encoder = RLEncoder()
    encoded_data = encoder.encode()
    print(json.dumps(encoded_data))