class FloatAnalyzer:
    def get_max(self, float_tuple):
        if not float_tuple:
            raise ValueError("Input tuple cannot be empty")
        return max(float_tuple)

if __name__ == '__main__':
    analyzer = FloatAnalyzer()
    sample_values_1 = (3.5, 2.1, 4.8, 1.9)
    sample_values_2 = (0.7, -1.2, -3.4, 2.5)
    sample_values_3 = (10.0,)
    empty_tuple = ()
    max1 = analyzer.get_max(sample_values_1)
    print(f"Maximum of {sample_values_1}: {max1}")
    max2 = analyzer.get_max(sample_values_2)
    print(f"Maximum of {sample_values_2}: {max2}")
    max3 = analyzer.get_max(sample_values_3)
    print(f"Maximum of {sample_values_3}: {max3}")