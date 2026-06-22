def check_all_same(values):
    if not values:
        return True
    first = values[0]
    return all(v == first for v in values)

if __name__ == '__main__':
    sample_list = [True, True, True]
    result = check_all_same(sample_list)
    print(result)