class ValueComparator:
    NUMERIC_TYPES = (int, float)
    STRING_TYPES = (str,)
    
    @staticmethod
    def is_numeric(value):
        return isinstance(value, ValueComparator.NUMERIC_TYPES)
    
    @staticmethod
    def is_string(value):
        return isinstance(value, ValueComparator.STRING_TYPES)
    
    def compare_values(self, val1, val2):
        if self.is_numeric(val1) and self.is_numeric(val2):
            return (val1 > val2, val1 < val2, val1 == val2)
        elif self.is_string(val1) and self.is_string(val2):
            return (val1 > val2, val1 < val2, val1 == val2)
        else:
            raise ValueError('Unsupported input types')

if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare_values(50, 20)
    result2 = comparator.compare_values('cat', 'dog')
    result3 = comparator.compare_values(7.5, 7.5)
    print(result1)
    print(result2)
    print(result3)