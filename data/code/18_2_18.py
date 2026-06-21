class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        
        encoded = []
        current_char = text[0]
        count = 1
        
        for char in text[1:]:
            if char == current_char:
                count += 1
            else:
                encoded.append(str(count))
                encoded.append(current_char)
                current_char = char
                count = 1
        
        encoded.append(str(count))
        encoded.append(current_char)
        
        return "".join(encoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    result = encoder.encode("aaabbccccddddd")
    print(result)