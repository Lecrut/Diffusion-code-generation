class RunLengthEncoder:
    SEPARATOR = "||"

    def __init__(self):
        self.encoding_log = []

    def encode(self, text: str) -> str:
        if not text:
            return ""
        
        encoded_chunks = []
        current_char = text[0]
        run_length = 1
        length = len(text)
        
        idx = 1
        while idx < length:
            char_at_idx = text[idx]
            if char_at_idx == current_char:
                run_length += 1
            else:
                encoded_chunks.append(str(run_length))
                encoded_chunks.append(self.SEPARATOR)
                encoded_chunks.append(current_char)
                encoded_chunks.append(self.SEPARATOR)
                current_char = char_at_idx
                run_length = 1
            idx += 1
            
        encoded_chunks.append(str(run_length))
        encoded_chunks.append(self.SEPARATOR)
        encoded_chunks.append(current_char)
        
        result = "".join(encoded_chunks)
        self.encoding_log.append(result)
        return result

if __name__ == '__main__':
    encoder = RunLengthEncoder()
    sample_text = "aaabbc"
    encoded_result = encoder.encode(sample_text)
    print(encoded_result)
    
    sample_text_2 = "xyz"
    encoded_result_2 = encoder.encode(sample_text_2)
    print(encoded_result_2)