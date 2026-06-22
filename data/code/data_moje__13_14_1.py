def get_from_generator(gen_expr, index):
    it = iter(gen_expr)
    for _ in range(index):
        next(it)
    return next(it)

if __name__ == '__main__':
    gen = (x ** 2 for x in range(10))
    result = get_from_generator(gen, 4)
    print(result)