def get_from_generator(gen_expr, index):
    it = iter(gen_expr)
    for i in range(index + 1):
        try:
            val = next(it)
        except StopIteration:
            return None
    return val

if __name__ == '__main__':
    result = get_from_generator((x * 2 for x in range(10)), 5)
    print(result)