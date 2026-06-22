class LargeIntegerSum:
    MAX_INT = 9223372036854775807
    
    @staticmethod
    def sum_large_integers(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both arguments must be integers.")
        return a + b
    
if __name__ == '__main__':
    instance = LargeIntegerSum()
    result = instance.sum_large_integers(12345678901234567890, 98765432109876543210)
    print(result)