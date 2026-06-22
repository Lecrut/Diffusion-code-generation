def find_the_middle_value_among_three_transform(a, b, c):
    numbers = sorted([a, b, c])
    return numbers[1]

if __name__ == '__main__':
    median = find_the_middle_value_among_three_transform(5, 3, 9)
    print(median)