import itertools

class StreamRLE:
    COMPRESSION_THRESHOLD = 2

    def __init__(self, source):
        self.source = source

    def compress_generator(self):
        if not self.source:
            return
        groups = itertools.groupby(self.source)
        for char, group_iter in groups:
            count = sum(1 for _ in group_iter)
            yield f"{count}{char}"

    def compress(self):
        return "".join(self.compress_generator())

    def decompress_generator(self, compressed):
        if not compressed:
            return
        number_buffer = []
        for char in compressed:
            if char.isdigit():
                number_buffer.append(char)
            else:
                if number_buffer:
                    count = int("".join(number_buffer))
                    number_buffer = []
                    for _ in range(count):
                        yield char
                else:
                    yield char
        if number_buffer:
            raise ValueError("Invalid compressed format: trailing numbers without character")

    def decompress(self, compressed):
        return "".join(self.decompress_generator(compressed))

if __name__ == '__main__':
    engine = StreamRLE("AAABBBCCCCD")
    compressed_data = engine.compress()
    print(compressed_data)
    decompressed_data = engine.decompress(compressed_data)
    print(decompressed_data)
    original = "Hello World"
    print(engine.compress())
    print(engine.decompress("1H1e2l1o1 1W1o2r1d"))
    complex_string = "AAAAAAAAABBBBBBBBBBCCCCCCCCCC"
    print(engine.compress())
    print(engine.decompress(engine.compress()))