class FloatAnalyzer:
    @staticmethod
    def get_max(floats):
        if not floats:
            raise ValueError("Input tuple cannot be empty")
        return max(floats)

if __name__ == '__main__':
    analyzer = FloatAnalyzer()
    sample_tuple_1 = (3.5, 2.1, 4.8, 1.9)
    sample_tuple_2 = (-10.5, -5.2, -20.7, -1.1)
    print(f"Maximum of {sample_tuple_1}: {analyzer.get_max(sample_tuple_1)}")
    print(f"Maximum of {sample_tuple_2}: {analyzer.get_max(sample_tuple_2)}")