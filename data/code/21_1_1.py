def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    val3 = 15
    print(find_max_of_three(val1, val2, val3))