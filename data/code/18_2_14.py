class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        if len(text) == 1:
            return f"{text}1"
        
        parts = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                parts.append(str(count))
                parts.append(current_char)
                current_char = char
                count = 1
        
        parts.append(str(count))
        parts.append(current_char)
        
        return "".join(parts)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    result = encoder.encode("AAABBBCCD")
    print(result)