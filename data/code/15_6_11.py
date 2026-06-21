def compress_sequence(source_string):
    compressed_chunks = []
    count = 1
    current_char = source_string[0]

    for index in range(1, len(source_string)):
        next_char = source_string[index]
        if next_char == current_char:
            count += 1
        else:
            compressed_chunks.append((count, current_char))
            count = 1
            current_char = next_char

    compressed_chunks.append((count, current_char))

    class RunLengthIterator:
        def __init__(self, chunks):
            self.chunks = chunks
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= len(self.chunks):
                raise StopIteration
            run_count, char = self.chunks[self.index]
            self.index += 1
            return run_count, char

    return RunLengthIterator(compressed_chunks)

if __name__ == '__main__':
    source = 'zzzzzxyyy'
    iterator = compress_sequence(source)
    results = []
    for count, char in iterator:
        results.append((count, char))
    print(results)