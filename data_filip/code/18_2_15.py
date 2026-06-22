class RunLengthEncoder:
    def encode(self, text):
        if not text:
            return ""
        
        result = []
        current_char = text[0]
        count = 1
        
        for i in range(1, len(text)):
            char = text[i]
            if char == current_char:
                count += 1
            else:
                result.append(current_char)
                result.append(str(count))
                current_char = char
                count = 1
        
        result.append(current_char)
        result.append(str(count))
        
        return "".join(result)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_string = "aaabbccccdd"
    encoded_result = encoder.encode(sample_string)
    print(encoded_result)
    
    sample_string_2 = "wwwwaaadexxxxxx"
    encoded_result_2 = encoder.encode(sample_string_2)
    print(encoded_result_2)
    
    sample_string_3 = ""
    encoded_result_3 = encoder.encode(sample_string_3)
    print(encoded_result_3)
    
    sample_string_4 = "a"
    encoded_result_4 = encoder.encode(sample_string_4)
    print(encoded_result_4)