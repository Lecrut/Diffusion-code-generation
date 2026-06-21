class TupleAnalyzer:
    def find_max(self, float_tuple):
        if not float_tuple:
            raise ValueError("Input tuple cannot be empty")
        return max(float_tuple)

if __name__ == '__main__':
    analyzer = TupleAnalyzer()
    sample_tuple1 = (3.5, 2.1, 4.8, 1.9)
    sample_tuple2 = (-0.5, -2.3, -1.7)
    sample_tuple3 = (100.0,)
    empty_tuple = ()
    
    max1 = analyzer.find_max(sample_tuple1)
    print(f"Maximum of {sample_tuple1}: {max1}")
    max2 = analyzer.find_max(sample_tuple2)
    print(f"Maximum of {sample_tuple2}: {max2}")
    max3 = analyzer.find_max(sample_tuple3)
    print(f"Maximum of {sample_tuple3}: {max3}")