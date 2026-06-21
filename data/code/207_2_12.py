class TupleMaxFinder:
    def find_max(self, float_tuple):
        return max(float_tuple)

if __name__ == '__main__':
    finder = TupleMaxFinder()
    sample_values_1 = (3.5, 2.1, 4.8, 1.9)
    sample_values_2 = (-3.2, -6.7, -2.1, -4.8)
    sample_values_3 = (0.0, 0.0, 0.0)
    
    max1 = finder.find_max(sample_values_1)
    print(f"Maximum of {sample_values_1}: {max1}")
    max2 = finder.find_max(sample_values_2)
    print(f"Maximum of {sample_values_2}: {max2}")
    max3 = finder.find_max(sample_values_3)
    print(f"Maximum of {sample_values_3}: {max3}")