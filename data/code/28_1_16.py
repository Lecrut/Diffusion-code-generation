MAX_VALUE = 100
MIN_VALUE = 1

def arrange_descending(val_one, val_two):
    first = MAX_VALUE
    second = MIN_VALUE
    if val_one > val_two:
        first = val_one
        second = val_two
    else:
        first = val_two
        second = val_one
    return first, second

if __name__ == '__main__':
    num_a = 42
    num_b = 17
    high, low = arrange_descending(num_a, num_b)
    print((high, low))