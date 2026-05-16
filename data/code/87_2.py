def check_both_true(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    value1 = True
    value2 = True
    result1 = check_both_true(value1, value2)
    print(f"check_both_true({value1}, {value2}) is: {result1}")
    value3 = True
    value4 = False
    result2 = check_both_true(value3, value4)
    print(f"check_both_true({value3}, {value4}) is: {result2}")
    value5 = False
    value6 = False
    result3 = check_both_true(value5, value6)
    print(f"check_both_true({value5}, {value6}) is: {result3}")
    value7 = True
    value8 = True
    result4 = check_both_true(value7, value8)
    print(f"check_both_true({value7}, {value8}) is: {result4}")