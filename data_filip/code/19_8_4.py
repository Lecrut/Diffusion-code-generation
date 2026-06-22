def _encode_sequence(run_char, run_count):
    return f"{run_char}{run_count}"

def _process_buffer(buffer, chunk_size):
    if len(buffer) >= chunk_size:
        result = "".join(buffer)
        buffer.clear()
        return result
    return None

class StreamRLEProcessor:
    def __init__(self, chunk_size=10):
        self.chunk_size = chunk_size
        self.buffer = []
        self.current_char = None
        self.run_count = 0

    def _flush_if_needed(self, char):
        if self.current_char is not None:
            self.buffer.append(_encode_sequence(self.current_char, self.run_count))
            self.current_char = char
            self.run_count = 1
        else:
            self.current_char = char
            self.run_count = 1
            return None
        
        encoded = _process_buffer(self.buffer, self.chunk_size)
        return encoded

    def process_stream(self, iterable):
        for char in iterable:
            if char == self.current_char:
                self.run_count += 1
            else:
                encoded = self._flush_if_needed(char)
                if encoded is not None:
                    yield encoded
        
        if self.current_char is not None:
            self.buffer.append(_encode_sequence(self.current_char, self.run_count))
            if self.buffer:
                yield "".join(self.buffer)
        
        self.buffer = []
        self.current_char = None
        self.run_count = 0

if __name__ == '__main__':
    sample_data = "AAAAAABBBBBBBCCCCCCCCDDDDDDDDD"
    processor = StreamRLEProcessor(chunk_size=3)
    for chunk in processor.process_stream(sample_data):
        print(chunk)