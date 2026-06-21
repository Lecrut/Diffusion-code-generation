def get_greatest_value(a, b, c):
    for arg in (a, b, c):
        if not isinstance(arg, (int, float)):
            raise TypeError("Arguments must be numeric")
    candidates = [a, b, c]
    current_max = candidates[0]
    index = 1
    while index < len(candidates):
        val = candidates[index]
        if val > current_max:
            current_max = val
        index += 1
    return current_max

if __name__ == '__main__':
    val_1 = 45
    val_2 = 12
    val_3 = 99
    result = get_greatest_value(val_1, val_2, val_3)
    print(result)