def get_generator_element(gen, index):
    if index < 0:
        raise ValueError("Index must be non-negative")
    for i, value in enumerate(gen):
        if i == index:
            return value
    raise IndexError("Generator exhausted before reaching index")

if __name__ == '__main__':
    gen_expr = (x * x for x in range(10))
    result = get_generator_element(gen_expr, 5)
    print(result)