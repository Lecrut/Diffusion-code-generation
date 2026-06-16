class PositiveValueValidator:
    def __init__(self):
        pass
    @staticmethod
    def _is_finite(value) -> bool:
        try:
            return not isinstance(value, float) and hasattr(value, '__float__')\
                or isinstance(value, float) and math.isfinite(value)
        except TypeError:
            return False
    def _is_positive(self, value):
        import math
        try:
            num = float(value)
        except (ValueError, TypeError):
            return False
        if math.isnan(num):
            return False
        if math.isinf(num):
            return num > 0
        return num > 0
    def is_positive(self, value) -> bool:
        try:
            return self._is_positive(value)
        except Exception as e:
            raise TypeError(f"Invalid input type for validation. Error details: {e}")
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [
        10,                                   
        -5,                                               
        3.14,                               
        -2.718,                                         
        float('nan'),                              
        float('-inf'),                                     
        float('+inf'),                                                                                                                                           
        0,                                    
    ]
    print("Validation Results:")
    for value in test_cases:
        result = validator.is_positive(value)
        status = "PASS" if result else "FAIL"
        print(f"Value {value!r}: {status}")