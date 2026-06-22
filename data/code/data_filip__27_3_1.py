class RLEncoder:
    def __init__(self):
        self.sample_string = "AAABBBCCDAA"

    def encode(self):
        if not self.sample_string:
            return []

        result = []
        i = 0
        n = len(self.sample_string)

        while i < n:
            current_char = self.sample_string[i]
            count = 1

            while i + count < n and self.sample_string[i + count] == current_char:
                count += 1

            result.append({
                "character": current_char,
                "count": count
            })

            i += count

        return result

if __name__ == '__main__':
    encoder = RLEncoder()
    encoded_result = encoder.encode()
    print(encoded_result)