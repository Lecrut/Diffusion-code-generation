def reverse_range_generator(start, end):
    for i in range(start, end - 1, -1):
        yield i
if __name__ == '__main__':
    start_value = 10
    end_value = 1
    generator = reverse_range_generator(start_value, end_value)
    result = list(generator)
    print(result)