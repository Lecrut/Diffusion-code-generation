def get_generator_element(gen_expr, index):
    for i, value in enumerate(gen_expr):
        if i == index:
            return value
    raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_gen = (x * x for x in range(10))
    result = get_generator_element(sample_gen, 5)
    print(result)