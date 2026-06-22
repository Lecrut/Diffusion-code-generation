def find_the_middle_value_among_three_compare():
    value1 = 5
    value2 = 3
    value3 = 4

    if (value1 >= value2 and value1 <= value3) or (value1 >= value3 and value1 <= value2):
        return value1
    elif (value2 >= value1 and value2 <= value3) or (value2 >= value3 and value2 <= value1):
        return value2
    else:
        return value3

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare()
    print(result)