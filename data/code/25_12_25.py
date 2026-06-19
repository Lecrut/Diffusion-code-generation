def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num == 0

if __name__ == '__main__':
    start = 0
    end = 10
    for result in even_number_generator(start, end):
        print(result)