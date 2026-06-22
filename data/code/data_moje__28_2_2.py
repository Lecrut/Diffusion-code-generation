def order_numbers(a, b):
    min_val = min(a, b)
    max_val = max(a, b)
    return min_val, max_val

if __name__ == '__main__':
    result = order_numbers(7, 2)
    print(result)