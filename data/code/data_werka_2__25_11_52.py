def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num == 0

if __name__ == '__main__':
    start = -3
    end = 7
    results = list(even_zero_generator(start, end))
    print(results)