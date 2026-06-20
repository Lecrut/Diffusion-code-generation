class PositiveChecker:
    def is_positive_and_below_100(self, value: float) -> bool:
        return 0 < value < 100

if __name__ == '__main__':
    checker = PositiveChecker()
    
    result1 = checker.is_positive_and_below_100(50)
    print(f"is_positive_and_below_100(50): {result1}")
    
    result2 = checker.is_positive_and_below_100(-10)
    print(f"is_positive_and_below_100(-10): {result2}")
    
    result3 = checker.is_positive_and_below_100(100)
    print(f"is_positive_and_below_100(100): {result3}")
    
    result4 = checker.is_positive_and_below_100(99.999)
    print(f"is_positive_and_below_100(99.999): {result4}")