class RunLengthEncoder:
    def encode(self, text: str) -> str:
        if not text:
            return ""
        if len(text) == 1:
            return "1" + text

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

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode("AAAABBBCCDAA"))
    print(encoder.encode("A"))
    print(encoder.encode(""))
    print(encoder.encode("ABC"))
    print(encoder.encode("AAAA"))