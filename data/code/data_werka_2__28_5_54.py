def compare_and_report(num1: float, num2: float) -> bool:
    STRICTLY_GREATER = 1
    EQUAL = 0
    STRICTLY_LESSER = -1
    
    def compare_numbers(a: float, b: float) -> int:
        if a > b:
            return STRICTLY_GREATER
        elif a < b:
            return STRICTLY_LESSER
        else:
            return EQUAL
    
    return compare_numbers(num1, num2) == STRICTLY_GREATER

if __name__ == '__main__':
    result = compare_and_report(7.0, 5.5)
    print(result)