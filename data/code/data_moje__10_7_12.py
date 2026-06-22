def integer_generator():
    for i in range(5):
        yield i

if __name__ == '__main__':
    gen = integer_generator()
    first_value = next(gen)
    print(first_value)