class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        
        result = []
        count = 1
        current_char = text[0]
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                if count > 1:
                    result.append(str(count))
                result.append(current_char)
                current_char = char
                count = 1
        
        if count > 1:
            result.append(str(count))
        result.append(current_char)
        
        return "".join(result)

    def decode(self, text: str) -> str:
        if not text:
            return ""
        
        result = []
        current_num = []
        
        for char in text:
            if char.isdigit():
                current_num.append(char)
            else:
                if current_num:
                    count = int("".join(current_num))
                    result.append(char * count)
                    current_num = []
                else:
                    result.append(char)
        
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_text = "AAABBBCCCA"
    encoded = encoder.encode(sample_text)
    print(encoded)
    decoded = encoder.decode(encoded)
    print(decoded)
    print(sample_text == decoded)