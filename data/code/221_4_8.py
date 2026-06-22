def order_numbers(a, b, c):
    min_val = a if a < b else b
    if min_val > c:
        min_val, c = c, min_val
    max_val = a if a > b else b
    if max_val < c:
        max_val, c = c, max_val
    mid_val = c
    return min_val, mid_val, max_val

if __name__ == '__main__':
    print(order_numbers(2.718, 3.141, 1.618))