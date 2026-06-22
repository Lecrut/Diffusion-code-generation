def even_zero_generator(start, end):
    for num in range(start, end + 1):
        if num == 0:
            yield True
        elif num % 2 != 0:
            continue
        else:
            yield False

if __name__ == '__main__':
    start = -3
    end = 7
    for result in even_zero_generator(start, end):
        print(result)