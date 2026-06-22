class RunLengthEncoder:
    @staticmethod
    def encode(input_string):
        if not input_string:
            return ""
        encoded = []
        count = 1
        for i in range(1, len(input_string)):
            if input_string[i] == input_string[i - 1]:
                count += 1
            else:
                encoded.append(f"{count}{input_string[i - 1]}")
                count = 1
        encoded.append(f"{count}{input_string[-1]}")
        return "".join(encoded)

    @staticmethod
    def decode(input_string):
        if not input_string:
            return ""
        decoded = []
        count = ""
        for char in input_string:
            if char.isdigit():
                count += char
            else:
                decoded.append(char * int(count))
                count = ""
        return "".join(decoded)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDA"
    encoder = RunLengthEncoder()
    encoded_result = encoder.encode(sample_data)
    decoded_result = encoder.decode(encoded_result)
    print(encoded_result)
    print(decoded_result)