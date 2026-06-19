def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num == 0 or (num % 2 == 0 and num != 0):
            yield True

if __name__ == '__main__':
    start = -5
    end = 5
    for result in even_zero_generator(start, end):
        print(result)