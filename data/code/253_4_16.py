MIDDLE_VALUE_INDEX = 1

def find_the_middle_value_among_three_summary(a, b, c):
    return sorted([a, b, c])[MIDDLE_VALUE_INDEX]

if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    print(find_the_middle_value_among_three_summary(a, b, c))