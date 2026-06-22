import json

class RLEEncoder:
    def __init__(self, text):
        self.text = text

    def encode(self):
        encoded = []
        length = len(self.text)
        index = 0

        while index < length:
            current_char = self.text[index]
            count = 0
            
            while index < length and self.text[index] == current_char:
                count += 1
                index += 1
            
            encoded.append({
                'char': current_char,
                'count': count
            })
        
        return encoded

if __name__ == '__main__':
    sample_text = "AAABBBCC"
    encoder = RLEEncoder(sample_text)
    result = encoder.encode()
    print(json.dumps(result))