def compare_integers(quantity1: int, quantity2: int) -> bool:
    return quantity1 > quantity2

if __name__ == '__main__':
    value1 = 42
    value2 = 37
    result = compare_integers(value1, value2)
    print(f"Is {value1} greater than {value2}? {result}")