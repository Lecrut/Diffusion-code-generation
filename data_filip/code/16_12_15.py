class RunLengthEncoder:
    def encode(self, data: str) -> list:
        if not data:
            return []
        
        result = []
        current_char = data[0]
        count = 1
        
        for i in range(1, len(data)):
            char = data[i]
            if char == current_char:
                count += 1
            else:
                result.append((current_char, count))
                current_char = char
                count = 1
        
        result.append((current_char, count))
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    print(encoder.encode("AAABBBCCC"))
    print(encoder.encode("Z"))
    print(encoder.encode(""))
    print(encoder.encode("ABC"))