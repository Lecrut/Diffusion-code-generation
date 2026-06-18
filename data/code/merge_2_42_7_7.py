import sys
def read_file_chunked(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield (line.strip(),)
def sort_large_dataset():
    data_gen = read_file_chunked('input.txt')
    def merge_sort(data):
        if len(list(data)) <= 1:
            return list(data)
        sorted_left, sorted_right = None, None
        left_gen = data_gen.__iter__()
        right_gen = iter([])
        try:
            first_item = next(left_gen)
            while True:
                second_item = next(right_gen, None)
                if second_item is not None:
                    sorted_right.append(first_item[0])
                    left_gen.send(second_item)
                    pass
                first_item = next(left_gen, None)
                if first_item is None:
                    break
            return sorted_left + sorted_right
        except StopIteration:
            return []
    def efficient_sort(data):
        return sorted(list(data))
    if __name__ == '__main__':
        try:
            with open('input.txt', 'r') as f:
                content = f.read().splitlines()
            data_gen = (line.strip() for line in content if line.strip())
            sorted_data = efficient_sort(data_gen)
            print('\n'.join(sorted_data))
        except FileNotFoundError:
            pass