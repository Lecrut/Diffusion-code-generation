def largest_of_three(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = largest_of_three(3.14, 2.71, 4.15)
    print(result)