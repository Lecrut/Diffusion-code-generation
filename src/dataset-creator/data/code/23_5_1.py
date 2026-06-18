def distinct_count_generator(input_list):
    seen = set()
    for item in input_list:
        if item not in seen:
            seen.add(item)
            yield 1
    return
if __name__ == '__main__':
    sample_list = [1, 2, 3, 1, 4, 2, 5, 3]
    count_generator = distinct_count_generator(sample_list)
    result_list = []
    for count in count_generator:
        result_list.append(count)
    print(result_list)