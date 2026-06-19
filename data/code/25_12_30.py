def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number == 0

if __name__ == '__main__':
    start = 0
    end = 10
    generator = even_number_generator(start, end)
    for result in generator:
        print(result)