def greatest_of_three(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    print(greatest_of_three(1, 2, 3))
    print(greatest_of_three(3, 1, 2))
    print(greatest_of_three(2, 3, 1))
    print(greatest_of_three(5, 5, 5))
    print(greatest_of_three(-1, -2, -3))
    print(greatest_of_three(0, -1, 1))
    print(greatest_of_three(10, 20, 15))