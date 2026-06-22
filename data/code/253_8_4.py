def find_the_middle_value_among_three_compare(x, y):
    return sorted([x, y])[1]

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)