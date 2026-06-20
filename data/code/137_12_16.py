def max_of_three(a, b, c):
    return a > b and a > c and a or (b > c and b or c)
if __name__ == '__main__':
    result = max_of_three(10, 20, 30)
    print(result)