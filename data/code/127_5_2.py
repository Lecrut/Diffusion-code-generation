def odd_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield True
if __name__ == '__main__':
    start_val = 1
    end_val = 10
    generator = odd_generator(start_val, end_val)
    result = list(generator)
    print(result)