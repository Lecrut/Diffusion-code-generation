import json

class RLEncoder:
    def __init__(self, sample_string):
        self.sample_string = sample_string

    def encode(self):
        if not self.sample_string:
            return []

        result = []
        current_char = self.sample_string[0]
        count = 1
        index = 1

        while index < len(self.sample_string):
            if self.sample_string[index] == current_char:
                count += 1
            else:
                result.append([current_char, count])
                current_char = self.sample_string[index]
                count = 1
            index += 1

        result.append([current_char, count])
        return result

if __name__ == '__main__':
    sample = "AAABBBCCCDDDDD"
    encoder = RLEncoder(sample)
    encoded = encoder.encode()
    print(json.dumps(encoded))