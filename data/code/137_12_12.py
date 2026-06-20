def max_of_three(a, b, c):
    return (a if a > b else b) if a > c else (b if b > c else c)

if __name__ == '__main__':
    result = max_of_three(15, 20, 30)
    print(result)