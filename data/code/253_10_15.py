MIDDLE_VALUE = "The middle value is: "

def find_the_middle_value_among_three_calculate(a, b, c):
    if a <= b <= c or c <= b <= a:
        return MIDDLE_VALUE + str(b)
    elif b <= a <= c or c <= a <= b:
        return MIDDLE_VALUE + str(a)
    else:
        return MIDDLE_VALUE + str(c)

if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(5, 10, 7))