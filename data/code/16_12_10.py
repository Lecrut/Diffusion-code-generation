class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return []
        
        encoded = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = text[i]
                count = 1
        
        encoded.append((current_char, count))
        return encoded

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    result_empty = encoder.encode("")
    result_single = encoder.encode("A")
    result_standard = encoder.encode("AAAABBBCCDAA")
    print(result_empty)
    print(result_single)
    print(result_standard)