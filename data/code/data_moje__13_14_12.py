def get_generator_value(generator, index):
    if index < 0:
        raise IndexError("Index must be non-negative")
    current_index = 0
    try:
        while current_index < index:
            next(generator)
            current_index += 1
        return next(generator)
    except StopIteration:
        raise IndexError("Index out of range")

if __name__ == '__main__':
    gen_expr = (x * x for x in range(10))
    result = get_generator_value(gen_expr, 5)
    print(result)