import json
import collections

class RLEEncoder:
    def __init__(self):
        self.sample_string = "AAAABBBCCDAA"

    def encode(self, text=None):
        if text is None:
            text = self.sample_string
        
        result = []
        length = len(text)
        index = 0
        
        while index < length:
            current_char = text[index]
            count = 0
            
            while index < length and text[index] == current_char:
                count += 1
                index += 1
            
            result.append({"char": current_char, "count": count})
        
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    output = encoder.encode()
    print(json.dumps(output))