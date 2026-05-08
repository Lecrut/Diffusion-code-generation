def subtract(a, b):
    return a - b
if __name__ == '__main__':
    result1 = subtract(10, 5)
    print(f"10 - 5 = {result1}")
    result2 = subtract(5, 10)
    print(f"5 - 10 = {result2}")
    result3 = subtract(10, 10)
    print(f"10 - 10 = {result3}")
    result4 = subtract(-10, 5)
    print(f"-10 - 5 = {result4}")
    result5 = subtract(5, -10)
    print(f"5 - (-10) = {result5}")
    result6 = subtract(-10, -5)
    print(f"-10 - (-5) = {result6}")
    result7 = subtract(0, 7)
    print(f"0 - 7 = {result7}")
    result8 = subtract(7, 0)
    print(f"7 - 0 = {result8}")