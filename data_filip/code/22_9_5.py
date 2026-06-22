class RunLengthEncoding:
    def encode(self, input_string):
        if not input_string:
            return ""
        
        encoded = []
        current_char = input_string[0]
        count = 1
        
        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                encoded.append(f"{count}{current_char}")
                current_char = input_string[i]
                count = 1
        
        encoded.append(f"{count}{current_char}")
        return "".join(encoded)

    def decode(self, encoded_string):
        if not encoded_string:
            return ""
        
        decoded = []
        i = 0
        while i < len(encoded_string):
            count_str = []
            while i < len(encoded_string) and encoded_string[i].isdigit():
                count_str.append(encoded_string[i])
                i += 1
            count = int("".join(count_str))
            char = encoded_string[i]
            i += 1
            decoded.append(char * count)
        
        return "".join(decoded)

if __name__ == '__main__':
    rle = RunLengthEncoding()
    original = "AAAAABBBCCDAA"
    encoded = rle.encode(original)
    print(encoded)
    decoded = rle.decode(encoded)
    print(decoded)