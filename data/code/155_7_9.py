MAX_SAFE_INTEGER = 2**53 - 1

def sum_mixed_types(values):
    total = 0.0
    for value in values:
        if isinstance(value, int) and -MAX_SAFE_INTEGER <= value <= MAX_SAFE_INTEGER:
            total += float(value)
        elif isinstance(value, float) and -MAX_SAFE_INTEGER <= value <= MAX_SAFE_INTEGER:
            total += value
    return total

if __name__ == '__main__':
    my_list = [1, 5.5, 10, 2]
    print(sum_mixed_types(my_list))