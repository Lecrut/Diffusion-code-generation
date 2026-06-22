def greater_of_two(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    result = greater_of_two(10, 20)
    print(result)