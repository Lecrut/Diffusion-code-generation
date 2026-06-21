def combine_lists(large_list_a, large_list_b):
    it_a = iter(large_list_a)
    it_b = iter(large_list_b)
    while True:
        try:
            yield next(it_a)
        except StopIteration:
            for item in it_b:
                yield item
            break

if __name__ == '__main__':
    large_list_a = list(range(10))
    large_list_b = list(range(10, 20))
    combined_generator = combine_lists(large_list_a, large_list_b)
    result_list = [next(combined_generator) for _ in range(30)]
    print(result_list)