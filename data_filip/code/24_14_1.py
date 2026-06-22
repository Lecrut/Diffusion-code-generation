class RLE:
    def __init__(self):
        self.encoded = ""
        self.decoded = ""

    def encode(self, data):
        if not data:
            return ""
        encoded_chars = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded_chars.append(f"{count}{data[i - 1]}")
                count = 1
        encoded_chars.append(f"{count}{data[-1]}")
        self.encoded = "".join(encoded_chars)
        return self.encoded

    def decode(self, data):
        decoded_chars = []
        count_str = ""
        for char in data:
            if char.isdigit():
                count_str += char
            else:
                count = int(count_str)
                decoded_chars.append(char * count)
                count_str = ""
        self.decoded = "".join(decoded_chars)
        return self.decoded

if __name__ == '__main__':
    rle = RLE()
    sample_data = "AAAABBBCCDAA"
    result = rle.encode(sample_data)
    print(result)
    decoded_result = rle.decode(result)
    print(decoded_result)