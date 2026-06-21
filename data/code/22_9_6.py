class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        
        result = []
        count = 1
        current_char = text[0]
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = text[i]
                count = 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decode(self, text):
        if not text:
            return ""
        
        result = []
        count_str = ""
        
        for char in text:
            if char.isdigit():
                count_str += char
            else:
                count = int(count_str)
                result.append(char * count)
                count_str = ""
        
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "aabcccccaaa"
    encoded = encoder.encode(original)
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)