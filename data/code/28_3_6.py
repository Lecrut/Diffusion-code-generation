class RunLengthCompressor:
    DEFAULT_INPUT = "AABBBCCCCD"

    def __init__(self, data=None):
        self.data = data if data is not None else self.DEFAULT_INPUT

    @staticmethod
    def _calculate_runs(sequence):
        if not sequence:
            return dict()
        runs = dict()
        first = sequence[0]
        current_count = 1
        length = len(sequence)
        for idx in range(1, length):
            item = sequence[idx]
            if item == first:
                current_count += 1
            else:
                runs[first] = runs.get(first, 0) + current_count
                first = item
                current_count = 1
        runs[first] = runs.get(first, 0) + current_count
        return runs

    def compress(self):
        return self._calculate_runs(self.data)

if __name__ == '__main__':
    compressor = RunLengthCompressor("aaabbbcccaaa")
    print(compressor.compress())