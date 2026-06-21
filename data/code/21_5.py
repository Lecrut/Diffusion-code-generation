def largest_of_three(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    result = largest_of_three(x, y, z)
    print(result)