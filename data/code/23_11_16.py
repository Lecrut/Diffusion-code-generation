class RunLengthEncoder:
    def encode(self, input_string: str) -> str:
        if not input_string:
            return ""
        
        encoded_chars = []
        count = 1
        char_length = len(input_string)
        
        for index in range(1, char_length):
            current_char = input_string[index]
            previous_char = input_string[index - 1]
            
            if current_char == previous_char:
                count += 1
            else:
                encoded_chars.append(self._format_count(count))
                encoded_chars.append(previous_char)
                count = 1
        
        encoded_chars.append(self._format_count(count))
        encoded_chars.append(input_string[-1])
        
        return "".join(encoded_chars)
    
    def _format_count(self, count: int) -> str:
        if count > 1:
            return str(count)
        return ""

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_string = "AAABBBCCC"
    result = encoder.encode(sample_string)
    print(result)