def find_the_middle_value_among_three_compare(x, y):
    if x <= y:
        return y if y >= x else x
    else:
        return x if x >= y else y

if __name__ == '__main__':
    value1 = 9
    value2 = 5
    middle_value = find_the_middle_value_among_three_compare(value1, value2)
    print(middle_value)