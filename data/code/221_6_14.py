def sort_three_values(a, b, c):
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    middle_val = a + b + c - min_val - max_val
    return (min_val, middle_val, max_val)

if __name__ == '__main__':
    x = 7
    y = 3
    z = 5
    result = sort_three_values(x, y, z)
    print(result)