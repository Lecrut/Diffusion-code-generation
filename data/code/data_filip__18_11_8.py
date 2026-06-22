class RunLengthEncoder:
    @staticmethod
    def encode(data):
        if not data:
            return ""
        result = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(data[i - 1])
                count = 1
        result.append(str(count))
        result.append(data[-1])
        return "".join(result)

    @staticmethod
    def decode(data):
        if not data:
            return ""
        result = []
        i = 0
        while i < len(data):
            num_str = ""
            while i < len(data) and data[i].isdigit():
                num_str += data[i]
                i += 1
            if i < len(data):
                result.append(data[i] * int(num_str))
                i += 1
        return "".join(result)

    @staticmethod
    def encode_list(data):
        if not data:
            return []
        result = []
        count = 1
        for i in range(1, len(data)):
            if data[i] == data[i - 1]:
                count += 1
            else:
                result.append((count, data[i - 1]))
                count = 1
        result.append((count, data[-1]))
        return result

    @staticmethod
    def decode_list(encoded_data):
        result = []
        for count, char in encoded_data:
            result.extend([char] * count)
        return result

if __name__ == '__main__':
    test_strings = ["AAABBBCCD", "WWWWWWWWWWWWBWW", "111122222", ""]
    test_chars = [list("AAABBBCCD"), list("aaaaaaabbbbbbbbcccc")]
    
    for s in test_strings:
        encoded = RunLengthEncoder.encode(s)
        decoded = RunLengthEncoder.decode(encoded)
        print(f"String: {s}, Encoded: {encoded}, Decoded: {decoded}")

    for char_list in test_chars:
        encoded = RunLengthEncoder.encode_list(char_list)
        decoded = RunLengthEncoder.decode_list(encoded)
        print(f"List: {char_list}, Encoded: {encoded}, Decoded: {decoded}")