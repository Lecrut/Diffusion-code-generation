def get_from_generator(gen_func, index):
    iterator = iter(gen_func())
    for i in range(index + 1):
        try:
            value = next(iterator)
        except StopIteration:
            raise IndexError(f"Index {index} is out of range for the generator")
    return value

if __name__ == '__main__':
    gen_expr = (x * 2 for x in range(10))
    result = get_from_generator(lambda: gen_expr, 4)
    print(result)