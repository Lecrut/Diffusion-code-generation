import json

class RLEEncoder:
    def __init__(self, sample_string):
        self.sample_string = sample_string

    def encode(self):
        encoded_list = []
        length = len(self.sample_string)
        if length == 0:
            return encoded_list
        current_char = self.sample_string[0]
        count = 1
        i = 1
        while i < length:
            char = self.sample_string[i]
            if char == current_char:
                count += 1
            else:
                encoded_list.append({"char": current_char, "count": count})
                current_char = char
                count = 1
            i += 1
        encoded_list.append({"char": current_char, "count": count})
        return encoded_list

if __name__ == '__main__':
    encoder = RLEEncoder("AAABBBCCCC")
    result = encoder.encode()
    print(json.dumps(result))