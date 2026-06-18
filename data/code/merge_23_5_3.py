def distinct_count_generator(input_list):
    seen = set()
    for item in input_list:
        if item not in seen:
            seen.add(item)
            yield 1
    yield 0
if __name__ == '__main__':
    sample_list = [1, 2, 3, 1, 4, 2, 5, 3]
    count_generator = distinct_count_generator(sample_list)
    result = list(count_generator)
    print(result)