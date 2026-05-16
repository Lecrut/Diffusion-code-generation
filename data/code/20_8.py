if __name__ == '__main__':
    value1 = 10
    value2 = 10.0
    type1 = type(value1)
    type2 = type(value2)
    if type1 == type2:
        print("Values are equal and have the same type.")
    else:
        print("Values are not equal or do not have the same type.")