def max_of_three(a, b, c):
    return (a if a > b else b) if a > c else c
if __name__ == '__main__':
    result = max_of_three(10, 20, 15)
    print(result)