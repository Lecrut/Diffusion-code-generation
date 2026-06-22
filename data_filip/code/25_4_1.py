class RunLengthEncoder:
    def __init__(self):
        self.last_encoded = ""
        self.last_decoded = ""

    def encode(self, text):
        if not text:
            self.last_encoded = ""
            return ""
        encoded = []
        current_char = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = text[i]
                count = 1
        encoded.append(str(count) + current_char)
        self.last_encoded = "".join(encoded)
        return self.last_encoded

    def decode(self, encoded_text):
        if not encoded_text:
            self.last_decoded = ""
            return ""
        decoded = []
        i = 0
        while i < len(encoded_text):
            count_str = ""
            while i < len(encoded_text) and encoded_text[i].isdigit():
                count_str += encoded_text[i]
                i += 1
            if i >= len(encoded_text):
                raise ValueError("Invalid encoded format: missing character after count")
            count = int(count_str)
            char = encoded_text[i]
            decoded.append(char * count)
            i += 1
        self.last_decoded = "".join(decoded)
        return self.last_decoded

if __name__ == '__main__':
    rle = RunLengthEncoder()
    original_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = rle.encode(original_string)
    print(encoded_result)
    decoded_result = rle.decode(encoded_result)
    print(decoded_result)