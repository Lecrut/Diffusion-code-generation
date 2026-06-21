class RLEncoder:
    SAMPLE_STRING = 'AAAABBBCCDAA'

    def encode(self, data):
        if not data:
            return []
        result = []
        prev_char = data[0]
        char_count = 1
        for idx in range(1, len(data)):
            curr_char = data[idx]
            if curr_char == prev_char:
                char_count += 1
            else:
                result.append((prev_char, char_count))
                prev_char = curr_char
                char_count = 1
        result.append((prev_char, char_count))
        return result

if __name__ == '__main__':
    encoder = RLEncoder()
    output = encoder.encode(encoder.SAMPLE_STRING)
    print(output)