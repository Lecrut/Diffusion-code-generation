import functools
def dynamic_product(items: tuple) -> int:
    return functools.reduce(lambda x, y: x * y, items, 1)
if __name__ == '__main__':
    sample_items = (2, 3, 4, 5)
    result = dynamic_product(sample_items)
    print(result)