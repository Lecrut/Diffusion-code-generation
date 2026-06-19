def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield True

if __name__ == '__main__':
    start = 0
    end = 10
    generator = even_number_generator(start, end)
    for result in generator:
        print(result)