def conditional_sum(a: int | float, b: int | float, c: int | float) -> float:
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))) and\
       (isinstance(c, (int, float))):
        return a + b + c
    else:
        raise TypeError("All variables must be int or float")
if __name__ == '__main__':
    x = 10.5
    y = -3
    z = "hello"
    try:
        result = conditional_sum(x, y, z)
        print(result)
    except TypeError as e:
        print(e)