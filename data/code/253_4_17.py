def find_the_middle_value_among_three_summary(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    x = 42
    y = 7
    z = 36
    print(find_the_middle_value_among_three_summary(x, y, z))