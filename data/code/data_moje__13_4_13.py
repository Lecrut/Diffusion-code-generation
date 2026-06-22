def nth_element(gen, n):
    for i, value in enumerate(gen):
        if i == n:
            return value
    raise IndexError("Generator does not have an element at index {}".format(n))

if __name__ == '__main__':
    sample_gen = (x * x for x in range(100))
    result = nth_element(sample_gen, 4)
    print(result)