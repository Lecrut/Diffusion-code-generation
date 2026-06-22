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
                encoded.append(f"{count}{data[i - 1]}")
                count = 1
        encoded.append(f"{count}{data[-1]}")
        return "".join(encoded)

    def decode(self, encoded_data):
        if not encoded_data:
            return ""
        decoded = []
        i = 0
        while i < len(encoded_data):
            count_str = ""
            while i < len(encoded_data) and encoded_data[i].isdigit():
                count_str += encoded_data[i]
                i += 1
            if i < len(encoded_data):
                char = encoded_data[i]
                count = int(count_str)
                decoded.append(char * count)
                i += 1
        return "".join(decoded)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    original_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = encoder.encode(original_string)
    print(encoded_result)
    decoded_result = encoder.decode(encoded_result)
    print(decoded_result)