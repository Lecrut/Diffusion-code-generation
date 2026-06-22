def find_the_middle_value_among_three_summary(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_summary(3, 1, 2))
    print(find_the_middle_value_among_three_summary(10, 5, 20))
    print(find_the_middle_value_among_three_summary(10, 25, 15))