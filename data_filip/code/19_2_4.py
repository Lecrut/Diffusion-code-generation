class RLEEngine:
    def __init__(self, max_run_length: int = 1000000):
        self.max_run_length = max_run_length

    def compress(self, data: str) -> str:
        if not data:
            return ""
        result = []
        current_char = data[0]
        count = 1
        total_len = len(data)
        i = 1
        while i < total_len:
            char = data[i]
            if char == current_char and count < self.max_run_length:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
            i += 1
        result.append(f"{count}{current_char}")
        return "".join(result)

    def decompress(self, compressed: str) -> str:
        if not compressed:
            return ""
        result = []
        i = 0
        n = len(compressed)
        while i < n:
            start = i
            while i < n and compressed[i].isdigit():
                i += 1
            if i == start:
                raise ValueError(f"Invalid format at index {start}: expected digit")
            count_str = compressed[start:i]
            count = int(count_str)
            if i >= n:
                raise ValueError(f"Invalid format: missing character after count {count_str}")
            char = compressed[i]
            i += 1
            if char == '':
                raise ValueError("Empty character found in compressed data")
            result.append(char * count)
        return "".join(result)

def run_generator_compress(data: str, chunk_size: int = 100):
    if not data:
        return
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
            if count == chunk_size:
                yield f"{count}{current_char}"
                current_char = None
                count = 0
        else:
            if current_char is not None:
                yield f"{count}{current_char}"
            current_char = char
            count = 1
    if current_char is not None:
        yield f"{count}{current_char}"

def run_generator_decompress(compressed: str, buffer_limit: int = 1024):
    if not compressed:
        return
    i = 0
    n = len(compressed)
    current_buffer = []
    current_len = 0
    while i < n:
        start = i
        while i < n and compressed[i].isdigit():
            i += 1
        count = int(compressed[start:i])
        char = compressed[i]
        i += 1
        for _ in range(count):
            current_buffer.append(char)
            current_len += 1
            if current_len >= buffer_limit:
                yield "".join(current_buffer)
                current_buffer = []
                current_len = 0
    if current_buffer:
        yield "".join(current_buffer)

if __name__ == "__main__":
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    engine = RLEEngine()
    compressed = engine.compress(test_string)
    print(f"Original length: {len(test_string)}")
    print(f"Compressed: {compressed}")
    decompressed = engine.decompress(compressed)
    print(f"Decompressed matches original: {decompressed == test_string}")
    
    gen_compressed = list(run_generator_compress(test_string, 10))
    print(f"Generator compressed chunks: {gen_compressed}")
    
    gen_decompressed = list(run_generator_decompress(compressed, 5))
    print(f"Generator decompressed chunks: {gen_decompressed}")
    
    full_gen_decompressed = "".join(run_generator_decompress(compressed))
    print(f"Full generator decompress matches original: {full_gen_decompressed == test_string}")