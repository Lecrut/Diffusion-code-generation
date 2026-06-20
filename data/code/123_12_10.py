class FloatTupleSum:
    def sum_elements(self, float_tuple):
        return sum(float_tuple)

if __name__ == '__main__':
    calculator = FloatTupleSum()
    sample_tuple1 = (3.5, 2.1, 4.8)
    sample_tuple2 = (1.0, 2.0, 3.0, 4.0)
    
    result1 = calculator.sum_elements(sample_tuple1)
    result2 = calculator.sum_elements(sample_tuple2)
    
    print(f"Sum of {sample_tuple1}: {result1}")
    print(f"Sum of {sample_tuple2}: {result2}")