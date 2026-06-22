class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        if len(text) == 1:
            return text[0]
        
        result = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            if text[i] == current_char:
                count += 1
            else:
                result.append(str(count) + current_char)
                current_char = text[i]
                count = 1
        
        result.append(str(count) + current_char)
        return "".join(result)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_inputs = ["", "a", "aa", "aabbbcccc", "aaaabbbccccdddd", "11223334444"]
    
    for s in sample_inputs:
        encoded = encoder.encode(s)
        print(f"Input: '{s}' -> Encoded: '{encoded}'")