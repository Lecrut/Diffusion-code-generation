class RLEEncoder:
    def encode(self, data):
        if not data:
            return []
        result = []
        current_char = data[0]
        count = 1
        for char in data[1:]:
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RLEEncoder()
    sample1 = "aaabbbaac"
    sample2 = "a"
    sample3 = ""
    print(encoder.encode(sample1))
    print(encoder.encode(sample2))
    print(encoder.encode(sample3))