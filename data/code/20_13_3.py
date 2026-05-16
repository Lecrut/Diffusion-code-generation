def compare_values(a, b):
    if type(a) == type(b):
        if a == b:
            print("The two values are equal.")
        else:
            print("The two values are not equal.")
    else:
        print("Error: Cannot compare values of different types.")
if __name__ == '__main__':
    value1 = 10
    value2 = 10
    compare_values(value1, value2)
    value3 = "hello"
    value4 = "hello"
    compare_values(value3, value4)
    value5 = 5.5
    value6 = 5.50
    compare_values(value5, value6)
    value7 = 10
    value8 = "10"
    compare_values(value7, value8)