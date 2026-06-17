def find_middle_index(data):
    try:
        iterator = iter(data)
        count = 0
        total_length = 0
        while True:
            try:
                next(iterator)
                total_length += 1
            except StopIteration:
                break
        if total_length == 0:
            return -1
        middle_index = total_length // 2
    except TypeError:
        raise ValueError("Input must be an iterable sequence")
if __name__ == '__main__':
    sample_list = [0, 1, 2, 3, 4]
    result_index = find_middle_index(sample_list)
    print(f"Middle index: {result_index}")