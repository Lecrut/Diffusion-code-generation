def find_difference(num1, num2):
    return abs(num1 - num2)
if __name__ == '__main__':
    sample1 = (5, 3)
    sample2 = (10, 15)
    sample3 = (-7, -7)
    print(find_difference(*sample1))
    print(find_difference(*sample2))
    print(find_difference(*sample3))