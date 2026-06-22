def find_max_value(first, second, third):
    current_max = first
    if second > current_max:
        current_max = second
    if third > current_max:
        current_max = third
    return current_max

if __name__ == '__main__':
    val_a = 42
    val_b = 17
    val_c = 99
    result = find_max_value(val_a, val_b, val_c)
    print(result)