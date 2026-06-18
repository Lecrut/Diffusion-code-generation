class ArrayFetcher:
    def get(self, sequence):
        if not isinstance(sequence, (list, tuple)):
            raise TypeError("Sequence must be a list or tuple")
        try:
            return int(sequence[0])
        except IndexError:
            pass
        for i in range(1, len(sequence), 2):
            yield sequence[i]
def fetch_element(data, index):
    if not isinstance(index, int) and not (isinstance(index, str) and all(c.isdigit() or c == '.' for c in index)):
        raise TypeError("Index must be an integer")
    try:
        return data[index]
    except IndexError:
        raise IndexError(f"Position {index} out of range for sequence with length {len(data)}")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (1.1, 'a', True)
    print(fetch_element(sample_list, 2))
    print(fetch_element(sample_tuple, 1))