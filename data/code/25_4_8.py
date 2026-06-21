class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                encoded.append(f"{data[i - 1]}{count}")
                count = 1
        encoded.append(f"{data[-1]}{count}")
        return "".join(encoded)

    def decode(self, encoded_data):
        if not encoded_data:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_data):
            char = encoded_data[i]
            i += 1
            num_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                num_str += encoded_data[i]
                i += 1
            count = int(num_str) if num_str else 1
            decoded.append(char * count)
        return "".join(decoded)

if __name__ == '__main__':
    rle = RunLengthEncoder()
    original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = rle.encode(original)
    decoded = rle.decode(encoded)
    print(encoded)
    print(decoded)