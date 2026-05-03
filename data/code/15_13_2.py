def check_equal(a, b):
    return a == b
if __name__ == '__main__':
    result1 = check_equal(10, 10)
    result2 = check_equal("hello", "hello")
    result3 = check_equal([1, 2], [1, 2])
    result4 = check_equal(1, 2)
    print(f"10 == 10: {result1}")
    print(f"'hello' == 'hello': {result2}")
    print(f"[1, 2] == [1, 2]: {result3}")
    print(f"1 == 2: {result4}")