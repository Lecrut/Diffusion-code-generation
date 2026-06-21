import json

class RLEEncoder:
    def __init__(self, sample_string):
        self.sample_string = sample_string

    def encode(self):
        if not self.sample_string:
            return []
        
        result = []
        i = 0
        while i < len(self.sample_string):
            current_char = self.sample_string[i]
            count = 1
            j = i + 1
            while j < len(self.sample_string) and self.sample_string[j] == current_char:
                count += 1
                j += 1
            result.append([current_char, count])
            i = j
        
        return result

if __name__ == '__main__':
    encoder = RLEEncoder("AAABBCDDDEEFF")
    encoded_result = encoder.encode()
    print(json.dumps(encoded_result))