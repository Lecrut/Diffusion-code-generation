def max_of_three(a, b, c):
    return a if (a > b and a > c) else (b if b > c else c)

if __name__ == '__main__':
    print(max_of_three(10, 20, 30))