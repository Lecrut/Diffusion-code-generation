def greatest_of_three(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    result = greatest_of_three(10, 25, 15)
    print(result)