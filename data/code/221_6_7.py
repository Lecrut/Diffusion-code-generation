def find_middle(a, b):
    return a if a != min(a, b) and a != max(a, b) else b

def order_three(a, b, c):
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    middle_val = find_middle(a, b, c)
    return (min_val, middle_val, max_val)

if __name__ == '__main__':
    x = 5
    y = 2
    z = 8
    result = order_three(x, y, z)
    print(result)