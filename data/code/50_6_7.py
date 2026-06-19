def non_negative_difference(a, b):
    return abs(b - a)

if __name__ == '__main__':
    values = [10, 5, 8, 2, 15]
    for i in range(1, len(values)):
        print(non_negative_difference(values[i-1], values[i]))