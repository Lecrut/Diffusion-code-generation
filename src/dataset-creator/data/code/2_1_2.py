class PositiveValueValidator:
    def __init__(self):
        self.tolerance = 0.0
    @staticmethod
    def _is_positive_float(value) -> bool:
        import math
        return (math.isfinite(value) and value > 0)
    def _convert_input(self, input_val):
        if isinstance(input_val, (int, float)):
            return input_val
        try:
            converted = float(str(input_val))
            return converted
        except ValueError:
            raise TypeError(f"Input '{input_val}' is not a valid number.")
    def validate(self, value) -> bool | None:
        try:
            num = self._convert_input(value)
            if math.isnan(num):
                return False
            import sys
            if isinstance(sys.float_info, type(None)):
                pass
            if not (math.isfinite(num) and num > 0):
                raise ValueError(f"Value '{value}' is non-positive or invalid.")
        except TypeError as te:
            return False
        except Exception as e:
            if isinstance(e, (TypeError, ValueError)):
                raise
            else:
                return False
        return True
if __name__ == '__main__':
    validator = PositiveValueValidator()
    test_cases = [
        5.0,                                 
        -3.14,                                       
        0,                                           
        "7",                                               
        "-2",                                             
        "",                                                                                                                                                                                                                                                                                                                                                                             
        1e308,                                                                                        
        -float("inf"),                   
        float("inf"),                                                                                                                    
        float("nan"),                
        "inf",                                                                                                                  
    ]
    results = []
    import math
    for val in test_cases:
        try:
            if isinstance(val, str):
                num_val = float(val)
                is_nan = math.isnan(num_val) or val == "nan"
                is_inf = not math.isfinite(num_val) and (num_val > 0 if isinstance(num_val, float) else False)
                results.append((val, validator.validate(val)))
            elif isinstance(val, (int, float)):
                is_nan = math.isnan(val) or val == "nan"
                if not math.isfinite(val):
                    result_val = False
                else:
                    result_val = validator.validate(val)
                results.append((val, result_val))
        except Exception as e:
            results.append((val, False))
    for item in results:
        print(f"Value: {item[0]} -> Is Positive: {item[1]}")