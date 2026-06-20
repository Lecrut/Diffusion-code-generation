class SumCalculator:
    def calculate_sum(self, iterable):
        total = 0.0
        for item in iterable:
            total += item
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    float_tuple1 = (1.5, 2.5, 3.5)
    float_tuple2 = (4.5, 5.5, 6.5)
    empty_tuple = ()
    single_element_tuple = (7.0,)
    
    sum1 = calculator.calculate_sum(float_tuple1)
    sum2 = calculator.calculate_sum(float_tuple2)
    sum_empty = calculator.calculate_sum(empty_tuple)
    sum_single = calculator.calculate_sum(single_element_tuple)
    
    print(f"Sum of {float_tuple1}: {sum1}")
    print(f"Sum of {float_tuple2}: {sum2}")
    print(f"Sum of empty tuple: {sum_empty}")
    print(f"Sum of single element tuple: {sum_single}")