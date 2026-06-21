def find_max_of_three(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError("All inputs must be integers")
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    v1 = 7
    v2 = 19
    v3 = 12
    print(find_max_of_three(v1, v2, v3))