def sort_descending(a: float, b: float) -> tuple[float, float]:
    if a >= b:
        return a, b
    return b, a

if __name__ == '__main__':
    num1 = 15.5
    num2 = 23.7
    result = sort_descending(num1, num2)
    print(result)