def even_elements():
    numbers = [12, 14, 16, 18, 20]
    for number in numbers:
        if number % 2 == 0:
            yield number

if __name__ == '__main__':
    gen = even_elements()
    print(next(gen))
    print(next(gen))
    print(next(gen))