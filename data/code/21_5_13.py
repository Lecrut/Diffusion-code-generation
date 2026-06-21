def largest_of_three(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = largest_of_three(10, 5, 20)
    print(result)