def check_all_same_bools(values):
    if not values:
        return True
    first = values[0]
    for val in values[1:]:
        if val != first:
            return False
    return True

if __name__ == '__main__':
    sample_list = [True, True, True]
    result = check_all_same_bools(sample_list)
    print(result)