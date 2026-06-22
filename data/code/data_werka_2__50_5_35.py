def non_negative_difference(a, b):
    return max(0, a - b)

if __name__ == '__main__':
    x, y = 10, 25
    print(non_negative_difference(x, y))