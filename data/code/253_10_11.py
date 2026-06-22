MIDDLE_VALUE = "Middle Value"

def find_the_middle_value_among_three_calculate(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    result = find_the_middle_value_among_three_calculate(5, 2, 8)
    print(result)