class RunLengthEncoding:
    def encode(self, text: str) -> list[tuple[str, int]]:
        if not text:
            return []
        
        encoded = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = char
                count = 1
        
        encoded.append((current_char, count))
        return encoded

if __name__ == '__main__':
    encoder = RunLengthEncoding()
    result1 = encoder.encode("aabcccccaaa")
    print(result1)
    result2 = encoder.encode("")
    print(result2)
    result3 = encoder.encode("abc")
    print(result3)
    result4 = encoder.encode("a")
    print(result4)