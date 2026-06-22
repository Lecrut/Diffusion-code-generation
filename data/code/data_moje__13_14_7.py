def get_from_generator(gen, index):
    i = 0
    for item in gen:
        if i == index:
            return item
        i += 1
    raise IndexError("index out of range")

if __name__ == '__main__':
    gen = (x ** 2 for x in range(100))
    result = get_from_generator(gen, 10)
    print(result)