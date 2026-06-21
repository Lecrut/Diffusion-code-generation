def get_generator_element(gen, index):
    if index < 0:
        raise IndexError("Index must be non-negative")
    for i, value in enumerate(gen):
        if i == index:
            return value
    raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_gen = (x * x for x in range(10))
    result = get_generator_element(sample_gen, 5)
    print(result)
    sample_gen2 = (x for x in range(100))
    result2 = get_generator_element(sample_gen2, 0)
    print(result2)
    sample_gen3 = (x for x in range(100))
    result3 = get_generator_element(sample_gen3, 99)
    print(result3)