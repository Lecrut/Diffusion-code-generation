def get_value_from_generator(generator_expr, index):
    gen = generator_expr
    current_index = 0
    for value in gen:
        if current_index == index:
            return value
        current_index += 1
    return None

if __name__ == '__main__':
    gen = (x * 2 for x in range(10))
    result = get_value_from_generator(gen, 4)
    print(result)