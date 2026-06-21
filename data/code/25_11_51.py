def even_zero_generator(start, end):
    for num in range(start, end + 1):
        is_even = (num % 2 == 0)
        is_zero = (num == 0)
        yield is_even and is_zero

if __name__ == '__main__':
    start_value = -10
    end_value = 20
    for result in even_zero_generator(start_value, end_value):
        print(result)