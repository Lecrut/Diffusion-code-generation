def exceeds(quantity1: int, quantity2: int) -> bool:
    return quantity1 > quantity2

if __name__ == '__main__':
    sample1 = 10
    sample2 = 5
    result = exceeds(sample1, sample2)
    print(f"{sample1} exceeds {sample2}: {result}")