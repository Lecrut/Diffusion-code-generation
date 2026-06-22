def check_all_same_bool(values):
    if not values:
        return None
    first = values[0]
    for val in values[1:]:
        if val != first:
            return False
    return True

if __name__ == '__main__':
    sample_list = [True, True, True]
    result = check_all_same_bool(sample_list)
    print(result)