MIDDLE_INDEX = 1

def find_the_middle_value_among_three_compare(a, b):
    return sorted([a, b])[MIDDLE_INDEX]

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)