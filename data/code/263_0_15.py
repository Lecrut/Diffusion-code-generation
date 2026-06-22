def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

if __name__ == '__main__':
    result = max_of_three(10, 25, 10)
    print(result)