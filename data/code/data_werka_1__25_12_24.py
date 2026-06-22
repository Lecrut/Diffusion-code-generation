def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number == 0 or (number % 2 == 0 and number != 0):
            yield True

if __name__ == '__main__':
    start = 0
    end = 10
    generator = even_number_generator(start, end)
    for value in generator:
        print(value)