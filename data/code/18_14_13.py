def get_middle_value(items):
    n = len(items)
    if n == 0:
        raise ValueError("List must not be empty")
    return items[n // 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_middle_value(sample_list))