def count_elements_from_start(data):
    if not isinstance(data, list) or len(data) == 0:
        return 0
    counter = 0
    for _ in data:
        counter += 1
    return counter
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'a', None]
    result_count = count_elements_from_start(sample_list)
    print(f"Input list length: {len(sample_list)}")
    print(f"Counted elements from start: {result_count}")