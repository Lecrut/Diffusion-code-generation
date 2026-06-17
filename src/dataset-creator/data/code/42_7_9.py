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
                key = next_item.lower()
                value = None
            class Item:
                def __init__(self, k, v=None):
                    self.key = k
                    self.value = v
                def __repr__(self):
                    return f"Item({self.key})"
            item = Item(key) if isinstance(next_item, str) else next_item
            result.append(item)
    except StopIteration:
        pass
    return result
def main():
    data_gen = read_large_file('input.txt')
    sorted_items = list(sort_generator(data_gen))
    for item in sorted_items:
        print(item)
if __name__ == '__main__':
    pass