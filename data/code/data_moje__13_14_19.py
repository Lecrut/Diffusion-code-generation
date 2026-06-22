def get_generator_value(generator, index):
    for i, value in enumerate(generator):
        if i == index:
            return value
    raise IndexError("Index out of range")

if __name__ == '__main__':
    gen = (x ** 2 for x in range(10))
    result = get_generator_value(gen, 5)
    print(result)