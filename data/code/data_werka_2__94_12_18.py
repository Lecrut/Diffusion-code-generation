def has_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_list = [0, 0, 0, 1]
    result = has_truthy(sample_list)
    print(result)