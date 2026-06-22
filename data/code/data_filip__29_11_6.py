class RunLengthEncoder:
    def encode(self, input_string):
        if not input_string:
            return ""
        
        if len(input_string) == 1:
            return f"{input_string[0]}1"
        
        encoded_parts = []
        current_char = input_string[0]
        count = 1
        
        for i in range(1, len(input_string)):
            if input_string[i] == current_char:
                count += 1
            else:
                encoded_parts.append(f"{current_char}{count}")
                current_char = input_string[i]
                count = 1
        
        encoded_parts.append(f"{current_char}{count}")
        
        return "".join(encoded_parts)

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    test_cases = [
        "",
        "a",
        "aaabbbcccc",
        "abcdef",
        "aaabbbaacccbb"
    ]
    
    for case in test_cases:
        result = encoder.encode(case)
        print(f"Input: '{case}' -> Output: {result}")