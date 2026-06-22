def max_of_three(a, b, c):
    val = a
    if b > val:
        val = b
    if c > val:
        val = c
    return val

if __name__ == '__main__':
    test_values = [
        (10, 20, 5),
        (7, 7, 2),
        (-10, -30, -1),
        (100, 50, 200),
        (0, 0, 0)
    ]
    
    for x, y, z in test_values:
        print(max_of_three(x, y, z))