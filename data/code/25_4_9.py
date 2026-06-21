class RunLengthEncoder:
    def __init__(self):
        self.encoded_cache = ""
        self.decoded_cache = ""

    def encode(self, text):
        if not text:
            self.encoded_cache = ""
            return ""
        encoded_parts = []
        current_char = text[0]
        count = 1
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                encoded_parts.append(str(count) + current_char)
                current_char = char
                count = 1
        encoded_parts.append(str(count) + current_char)
        self.encoded_cache = "".join(encoded_parts)
        return self.encoded_cache

    def decode(self, encoded_text):
        if not encoded_text:
            self.decoded_cache = ""
            return ""
        decoded_parts = []
        i = 0
        n = len(encoded_text)
        while i < n:
            if not encoded_text[i].isdigit():
                count = 1
                char = encoded_text[i]
                i += 1
            else:
                j = i
                while j < n and encoded_text[j].isdigit():
                    j += 1
                count = int(encoded_text[i:j])
                char = encoded_text[j]
                i = j + 1
            decoded_parts.append(char * count)
        self.decoded_cache = "".join(decoded_parts)
        return self.decoded_cache

    def get_encoded(self):
        return self.encoded_cache

    def get_decoded(self):
        return self.decoded_cache

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    rle = RunLengthEncoder()
    encoded_result = rle.encode(sample_input)
    print(encoded_result)
    decoded_result = rle.decode(encoded_result)
    print(decoded_result)