def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num == 0

if __name__ == '__main__':
    start_value = -3
    end_value = 7
    results = list(even_zero_generator(start_value, end_value))
    print(results)