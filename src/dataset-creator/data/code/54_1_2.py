def calculate_center(iterable):
    try:
        iterator = iter(iterable)
        count = 0
        while True:
            item = next(iterator, None)
            if item is not None:
                count += 1
            else:
                break
    except StopIteration:
        return -1
    center_index = (count // 2) + ((count % 2))
    return center_index
if __name__ == '__main__':
    sample_sequence = [10, 20, 30]
    result = calculate_center(sample_sequence)
    print(result)