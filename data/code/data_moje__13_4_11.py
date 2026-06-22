def get_nth_element(generator, n):
    for i, item in enumerate(generator):
        if i == n:
            return item
    raise IndexError("Generator does not have enough elements")

if __name__ == '__main__':
    sample_gen = (x * 2 for x in range(10))
    result = get_nth_element(sample_gen, 5)
    print(result)