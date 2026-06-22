def compute_max(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    a, b = 5, 3
    max_value = compute_max(a, b)
    print(max_value)