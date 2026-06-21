def is_even(number: int) -> bool:
    return not (number & 1)

if __name__ == '__main__':
    result1 = is_even(4)
    result2 = is_even(7)
    print(result1)
    print(result2)