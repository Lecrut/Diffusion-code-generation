class RunLengthEncoder:
    def encode(self, data):
        if not data:
            return ""
        
        encoded = []
        current_char = data[0]
        count = 1
        
        for i in range(1, len(data)):
            if data[i] == current_char:
                count += 1
            else:
                encoded.append(str(count) + current_char)
                current_char = data[i]
                count = 1
        
        encoded.append(str(count) + current_char)
        return "".join(encoded)

if __name__ == "__main__":
    sample_string = "AAAABBBCCDA"
    encoder = RunLengthEncoder()
    result = encoder.encode(sample_string)
    print(result)