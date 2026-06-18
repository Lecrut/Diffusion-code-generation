def dynamic_product(items):
    result = 1
    for item in items:
        if isinstance(item, (int, float)):
            result *= item
    return result
if __name__ == '__main__':
    sample_tuple = (2, 3, 4)
    print(dynamic_product(sample_tuple))