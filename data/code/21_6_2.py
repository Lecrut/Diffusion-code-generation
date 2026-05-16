def reverse_range_generator(start, end):
    for i in range(start, end - 1, -1):
        yield i
if __name__ == '__main__':
    lower_bound = 10
    upper_bound = 25
    generator = reverse_range_generator(upper_bound, lower_bound)
    result = list(generator)
    print(result)