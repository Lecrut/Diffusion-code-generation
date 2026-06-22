def find_max_of_three(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    result = find_max_of_three(3.14, 2.71, 1.618)
    print(result)