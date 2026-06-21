class RunLengthEncoder:
    def __init__(self):
        self._buffer = []
    
    def _process_char(self, char, count):
        self._buffer.append(str(count))
        self._buffer.append(char)
    
    def encode(self, text):
        if not text:
            return ""
        self._buffer.clear()
        length = len(text)
        current_char = text[0]
        run_count = 1
        
        for i in range(1, length):
            next_char = text[i]
            if next_char == current_char:
                run_count += 1
            else:
                self._process_char(current_char, run_count)
                current_char = next_char
                run_count = 1
        
        self._process_char(current_char, run_count)
        return "".join(self._buffer)

if __name__ == "__main__":
    sample_string = "aaabbccccdddddee"
    encoder = RunLengthEncoder()
    result = encoder.encode(sample_string)
    print(result)