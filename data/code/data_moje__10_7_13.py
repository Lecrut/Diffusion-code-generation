def number_generator():
    yield 1
    yield 2
    yield 3

def main():
    gen = number_generator()
    first_value = next(gen)
    print(first_value)

if __name__ == '__main__':
    main()