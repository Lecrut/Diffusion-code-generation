class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        
        result = []
        current_char = text[0]
        count = 1
        length = len(text)
        
        for i in range(1, length):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        
        result.append(f"{count}{current_char}")
        
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode("AAAAABBBCCDE"))
    print(encoder.encode(""))
    print(encoder.encode("Z"))
    print(encoder.encode("AABBCA"))