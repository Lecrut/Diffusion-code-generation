class RunLengthEncoder:
    def __init__(self):
        self._output_buffer = []

    def _flush_run(self, char, count):
        self._output_buffer.append(str(count))
        self._output_buffer.append(char)

    def encode(self, text):
        if not text:
            return ""
        self._output_buffer.clear()
        length = len(text)
        idx = 0
        while idx < length:
            current_char = text[idx]
            run_length = 1
            idx += 1
            while idx < length and text[idx] == current_char:
                run_length += 1
                idx += 1
            self._flush_run(current_char, run_length)
        return "".join(self._output_buffer)

if __name__ == "__main__":
    encoder = RunLengthEncoder()
    sample_input = "aaabbbcccaaa"
    result = encoder.encode(sample_input)
    print(result)