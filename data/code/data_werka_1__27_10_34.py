class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2

if __name__ == '__main__':
    sample_value_1 = "hello"
    sample_value_2 = "world"
    sample_value_3 = 42
    sample_value_4 = 42.0
    
    checker = ValueChecker()
    
    result_1 = checker.are_different(sample_value_1, sample_value_2)
    print(f"are_different({sample_value_1}, {sample_value_2}): {result_1}")
    
    result_2 = checker.are_different(sample_value_3, sample_value_4)
    print(f"are_different({sample_value_3}, {sample_value_4}): {result_2}")
    
    result_3 = checker.are_different(True, False)
    print(f"are_different(True, False): {result_3}")
    
    result_4 = checker.are_different([1, 2, 3], [1, 2, 3])
    print(f"are_different({[1, 2, 3]}, {[1, 2, 3]}): {result_4}")