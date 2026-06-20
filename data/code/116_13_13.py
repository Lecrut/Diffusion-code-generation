def sum_three_integers(numbers: tuple[int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    result = sum_three_integers((1, 2, 3))
    print(result)