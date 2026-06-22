class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        if len(text) == 1:
            return text
        
        result = []
        count = 1
        current_char = text[0]
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(current_char)
                result.append(str(count))
                current_char = text[i]
                count = 1
        
        result.append(current_char)
        result.append(str(count))
        
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_inputs = ["", "a", "aa", "aabbbcccc", "AABBBBCCCCDD", "xyxyxy", "11122233"]
    
    for s in sample_inputs:
        encoded = encoder.encode(s)
        print(f"Input: '{s}' -> Encoded: '{encoded}'")