def indexed_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item
if __name__ == '__main__':
    data = list(range(1000000))
    target_index = 500000
    generator = indexed_generator(data, target_index)
    result = list(generator)
    print(f"Found element at index {target_index}: {result[0]}")