MIDDLE_VALUE_AMONG_THREE = 'Find the middle value among three'

def find_the_middle_value_among_three_calculate(a, b, c):
    return sorted([a, b, c])[1]
if __name__ == '__main__':
    result = find_the_middle_value_among_three_calculate(5, 3, 9)
    print(result)