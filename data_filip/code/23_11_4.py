class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        
        result = []
        count = 1
        char = text[0]
        
        for i in range(1, len(text)):
            if text[i] == char:
                count += 1
            else:
                result.append(f"{count}{char}")
                char = text[i]
                count = 1
        
        result.append(f"{count}{char}")
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "aaabbc"
    encoded_value = encoder.encode(sample_string)
    print(encoded_value)