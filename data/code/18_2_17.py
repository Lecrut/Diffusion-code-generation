class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ''

        encoded_chars = []
        current_char = text[0]
        count = 1

        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                encoded_chars.append(str(count))
                encoded_chars.append(current_char)
                current_char = text[i]
                count = 1

        encoded_chars.append(str(count))
        encoded_chars.append(current_char)

        return ''.join(encoded_chars)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_strings = [
        '',
        'a',
        'aaa',
        'aabbbcc',
        'aabbcc',
        'hello',
        'aabbcccdddd'
    ]

    for s in sample_strings:
        result = encoder.encode(s)
        print(f"'{s}' -> '{result}'")