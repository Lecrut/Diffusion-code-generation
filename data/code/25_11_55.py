def even_zero_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number == 0

if __name__ == '__main__':
    start_value = -10
    end_value = 5
    results = list(even_zero_generator(start_value, end_value))
    for result in results:
        print(result)