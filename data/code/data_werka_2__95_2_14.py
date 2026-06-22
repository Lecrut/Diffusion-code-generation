class TripleChecker:
    POSITIVE_EVEN_THRESHOLD = 0
    VALIDATION_ERROR_MSG = "All inputs must be positive integers."
    ZERO_DIVISION_MSG = "Third number cannot be zero."

    def validate(self, num1, num2, num3):
        if num1 <= self.POSITIVE_EVEN_THRESHOLD or num2 <= self.POSITIVE_EVEN_THRESHOLD or num3 <= self.POSITIVE_EVEN_THRESHOLD:
            raise ValueError(self.VALIDATION_ERROR_MSG)
        
        if num3 == 0:
            raise ZeroDivisionError(self.ZERO_DIVISION_MSG)
            
        is_first_even = num1 % 2 == 0
        is_second_even = num2 % 2 == 0
        
        if not (is_first_even and is_second_even):
            return False
            
        sum_first_two = num1 + num2
        is_divisible = sum_first_two % num3 == 0
        
        return is_divisible

if __name__ == '__main__':
    checker = TripleChecker()
    result_valid = checker.validate(2, 4, 6)
    print(result_valid)
    
    result_invalid_pos = checker.validate(-2, 4, 6)
    try:
        print(result_invalid_pos)
    except ValueError as e:
        print(f"ValueError: {e}")
        
    result_invalid_even = checker.validate(3, 4, 6)
    print(result_invalid_even)
    
    result_divisible_false = checker.validate(2, 4, 5)
    print(result_divisible_false)
    
    result_large = checker.validate(10, 20, 15)
    print(result_large)