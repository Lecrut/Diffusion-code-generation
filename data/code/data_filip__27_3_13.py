import json

class RLEEncoder:
    def __init__(self):
        self.sample_string = "aaabbccccddde"

    def encode(self):
        if not self.sample_string:
            return []
        
        result = []
        index = 0
        while index < len(self.sample_string):
            current_char = self.sample_string[index]
            count = 0
            while index < len(self.sample_string) and self.sample_string[index] == current_char:
                count += 1
                index += 1
            result.append({"char": current_char, "count": count})
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    encoded_result = encoder.encode()
    print(json.dumps(encoded_result))