class RunLengthEncoder:
    def __init__(self):
        self.encoded_string = ""
        self.decoded_string = ""

    def encode(self, text):
        if not text:
            self.encoded_string = ""
            return self.encoded_string
        encoded_chars = []
        count = 1
        current_char = text[0]
        index = 1
        text_length = len(text)
        while index < text_length:
            if text[index] == current_char:
                count += 1
            else:
                encoded_chars.append(str(count))
                encoded_chars.append(current_char)
                current_char = text[index]
                count = 1
            index += 1
        encoded_chars.append(str(count))
        encoded_chars.append(current_char)
        self.encoded_string = "".join(encoded_chars)
        return self.encoded_string

    def decode(self, text):
        if not text:
            self.decoded_string = ""
            return self.decoded_string
        decoded_chars = []
        text_length = len(text)
        index = 0
        while index < text_length:
            count_str = ""
            while index < text_length and text[index].isdigit():
                count_str += text[index]
                index += 1
            if index < text_length:
                char = text[index]
                index += 1
                if count_str:
                    count = int(count_str)
                    decoded_chars.append(char * count)
                else:
                    decoded_chars.append(char)
        self.decoded_string = "".join(decoded_chars)
        return self.decoded_string

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_input = "AAAABBBCCDAA"
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)