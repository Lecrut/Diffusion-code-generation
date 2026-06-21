class RunLengthEncoder:
    @staticmethod
    def encode(input_string: str) -> str:
        if not input_string:
            return ""
        
        compressed = []
        count = 1
        current_char = input_string[0]
        
        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                compressed.append(str(count) + current_char)
                current_char = input_string[i]
                count = 1
        compressed.append(str(count) + current_char)
        
        return ''.join(compressed)

    @staticmethod
    def decode(encoded_string: str) -> str:
        if not encoded_string:
            return ""
        
        decoded = []
        i = 0
        
        while i < len(encoded_string):
            num_str = []
            while i < len(encoded_string) and encoded_string[i].isdigit():
                num_str.append(encoded_string[i])
                i += 1
            count = int(''.join(num_str))
            char = encoded_string[i]
            decoded.append(char * count)
            i += 1
        
        return ''.join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder
    original = "AAAAABBBCCDEEE"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)