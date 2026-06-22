class ConditionChecker:
    _DEFAULT_THRESHOLD_LOWER = 0
    _DEFAULT_THRESHOLD_UPPER = 1000
    _DEFAULT_MODULUS = 7
    _DEFAULT_MULTIPLIER = 3

    def __init__(self, threshold_lower=None, threshold_upper=None, modulus=None, multiplier=None):
        lower = threshold_lower if threshold_lower is not None else self._DEFAULT_THRESHOLD_LOWER
        upper = threshold_upper if threshold_upper is not None else self._DEFAULT_THRESHOLD_UPPER
        mod = modulus if modulus is not None else self._DEFAULT_MODULUS
        mult = multiplier if multiplier is not None else self._DEFAULT_MULTIPLIER

        self._lower = lower
        self._upper = upper
        self._mod = mod
        self._mult = mult

    def check_all(self, value):
        is_positive = value > self._lower
        is_negative = value < self._upper
        is_divisible = value % self._mod == 0
        scaled_value = value * self._mult
        is_scaled_positive = scaled_value > 0
        
        all_results = [is_positive, is_negative, is_divisible, is_scaled_positive]
        
        for res in all_results:
            if not res:
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker(threshold_lower=10, threshold_upper=500, modulus=5, multiplier=2)
    sample_value = 20
    output = checker.check_all(sample_value)
    print(output)
    
    sample_value_2 = 15
    output_2 = checker.check_all(sample_value_2)
    print(output_2)
    
    sample_value_3 = 499
    output_3 = checker.check_all(sample_value_3)
    print(output_3)