import json
import copy

class RLEEncoder:
    def __init__(self):
        self.data = "WWWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"

    def encode(self):
        if not self.data:
            return []
        
        encoded_list = []
        index = 0
        length = len(self.data)
        
        while index < length:
            current_char = self.data[index]
            count = 0
            
            while index < length and self.data[index] == current_char:
                count += 1
                index += 1
            
            count_list = [c for c in str(count)]
            encoded_list.append(str(current_char))
            encoded_list.extend(count_list)
            
        return encoded_list

if __name__ == '__main__':
    encoder = RLEEncoder()
    result = encoder.encode()
    print(result)
    print(json.dumps(result))