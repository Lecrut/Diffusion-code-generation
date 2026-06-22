class RLEncoder:
    def __init__(self):
        self.sample_string = "AAABBBCCD"

    def encode(self):
        if not self.sample_string:
            return []
        result = []
        i = 0
        while i < len(self.sample_string):
            current_char = self.sample_string[i]
            count = 1
            while i + count < len(self.sample_string) and self.sample_string[i + count] == current_char:
                count += 1
            result.append([current_char, count])
            i += count
        return result

if __name__ == '__main__':
    encoder = RLEncoder()
    print(encoder.encode())