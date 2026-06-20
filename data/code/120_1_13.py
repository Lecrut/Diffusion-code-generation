def are_values_equal(value1, value2):
    return value1 == value2

if __name__ == '__main__':
    val1 = 3.14
    val2 = 3.14
    if are_values_equal(val1, val2):
        print("The values are equal.")
    else:
        print("The values are not equal.")