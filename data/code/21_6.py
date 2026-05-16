def reverse_range_generator(start, end):
    for i in range(start, end - 1, -1):
        yield i
if __name__ == '__main__':
    start_val = 10
    end_val = 1
    generator = reverse_range_generator(start_val, end_val)
    result = list(generator)
    print(result)