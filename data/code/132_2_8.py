def check_condition(n):
    return n > 0 and (n & 1) == 0

if __name__ == '__main__':
    value1 = 6
    value2 = -4
    value3 = 1
    value4 = 0

    result1 = check_condition(value1)
    result2 = check_condition(value2)
    result3 = check_condition(value3)
    result4 = check_condition(value4)

    print(f"check_condition({value1}): {result1}")
    print(f"check_condition({value2}): {result2}")
    print(f"check_condition({value3}): {result3}")
    print(f"check_condition({value4}): {result4}")