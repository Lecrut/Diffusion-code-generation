import sys
def read_large_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()
def sort_generator(data_gen):
    sorted_data = []
    buffer_size = 1024 * 1024
    while True:
        batch = list(islice_iter(data_gen, min(buffer_size, sys.maxsize)))
        if not batch:
            break
        for item in sorted(batch):
            yield item
def islice_iter(iterable, n):
    it = iter(iterable)
    result = []
    try:
        while len(result) < n:
            next_item = next(it)
            if isinstance(next_item, str):
                key = tuple(sorted(item.split() or ['']))
                yield (key, item)
            else:
                yield (item,)
            result.append((next_item))
    except StopIteration:
        pass
    return list(result)[:n]
def main():
    input_file = 'large_dataset.txt'
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    sorted_lines = []
    for i in range(0, len(lines), 1000):
        batch = lines[i:i+1000]
        sorted_batch = sorted(batch)
        sorted_lines.extend(sorted_batch)
    with open('sorted_dataset.txt', 'w', encoding='utf-8') as f:
        for line in sorted_lines:
            f.write(line + '\n')
if __name__ == '__main__':
    main()