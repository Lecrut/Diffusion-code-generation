def test_conditionals():
    a = 10
    b = 20
    c = 30
    if a > 15:
        result = "A is greater than 15"
    elif b > 15:
        result = "B is greater than 15"
    else:
        result = "Neither A nor B is greater than 15"
    if c == 30:
        status = "C is exactly 30"
    elif c < 30:
        status = "C is less than 30"
    else:
        status = "C is greater than 30"
    print(f"Test 1 Result: {result}")
    print(f"Test 2 Result: {status}")
if __name__ == '__main__':
    test_conditionals()