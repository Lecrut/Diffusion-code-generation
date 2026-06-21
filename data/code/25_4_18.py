class RunLengthEncoder:
    def encode(self, data: str) -> str:
        if not data:
            return ""
        
        encoded = []
        count = 1
        length = len(data)
        
        for i in range(length):
            if i + 1 < length and data[i] == data[i + 1]:
                count += 1
            else:
                encoded.append(str(count))
                encoded.append(data[i])
                count = 1
        
        return "".join(encoded)

    def decode(self, data: str) -> str:
        if not data:
            return ""
        
        decoded = []
        i = 0
        length = len(data)
        
        while i < length:
            num_str = ""
            while i < length and data[i].isdigit():
                num_str += data[i]
                i += 1
            
            if i < length:
                char = data[i]
                count = int(num_str)
                decoded.append(char * count)
                i += 1
        
        return "".join(decoded)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    original = "AAABBBCCCCDDDEEEE"
    encoded = encoder.encode(original)
    decoded = encoder.decode(encoded)
    print(encoded)
    print(decoded)