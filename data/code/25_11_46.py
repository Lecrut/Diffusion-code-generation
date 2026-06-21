def even_zero_generator(start, end):
    for number in range(start, end + 1):
        is_even = (number % 2 == 0)
        if is_even:
            yield (number == 0)

if __name__ == '__main__':
    range_start = -10
    range_end = 5
    for result in even_zero_generator(range_start, range_end):
        print(result)