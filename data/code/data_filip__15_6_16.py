class CharacterCompressor:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0
        self._compressed = self._compute_compressed()
        self._result_index = 0

    def _compute_compressed(self):
        if not self.sequence:
            return []
        compressed = []
        current_char = self.sequence[0]
        count = 1
        for char in self.sequence[1:]:
            if char == current_char:
                count += 1
            else:
                compressed.append((current_char, count))
                current_char = char
                count = 1
        compressed.append((current_char, count))
        return compressed

    def __iter__(self):
        return self

    def __next__(self):
        if self._result_index >= len(self._compressed):
            raise StopIteration
        char, count = self._compressed[self._result_index]
        self._result_index += 1
        return char, count

def compress_sequence(sequence):
    compressor = CharacterCompressor(sequence)
    result = []
    for char, count in compressor:
        result.append(f"{count}{char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = 'zzzzzxyyy'
    compressed_output = compress_sequence(sample_input)
    print(compressed_output)