import functools
def dynamic_product(items: tuple) -> int:
    return functools.reduce(lambda acc, val: acc * val, items, 1)
if __name__ == '__main__':
    sample_data = (2, 3, 4, 5)
    result = dynamic_product(sample_data)
    print(result)