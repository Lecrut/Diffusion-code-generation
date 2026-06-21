class RunLengthEncoder:
    def __init__(self):
        self.encoded_data = ""

    def encode(self, data):
        if not data:
            return ""
        result = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                result.append(str(count) + data[i - 1])
                count = 1
        result.append(str(count) + data[-1])
        return "".join(result)

    def decode(self, data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            count = int(num_str)
            if i < len(data):
                result.append(data[i] * count)
                i += 1
        return "".join(result)

    def get_encoded(self):
        return self.encoded_data

    def set_encoded(self, data):
        self.encoded_data = data

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_input)
    print(encoded_result)
    decoder = RunLengthEncoder()
    decoded_result = decoder.decode(encoded_result)
    print(decoded_result)