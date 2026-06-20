def calculate_weight_difference(a, b):
    diff = a - b
    if diff < 0:
        return -diff
    return diff

if __name__ == '__main__':
    val1 = 15.4
    val2 = 7.2
    result = calculate_weight_difference(val1, val2)
    print(result)