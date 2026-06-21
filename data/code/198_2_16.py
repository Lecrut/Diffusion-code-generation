class NumericStringAnalyzer:
    @staticmethod
    def convert_to_float(value):
        return float(value)

    @classmethod
    def get_minimum(cls, lst):
        if not lst:
            raise ValueError("List cannot be empty")
        converted_list = [cls.convert_to_float(x) for x in lst]
        minimum = min(converted_list)
        return minimum

if __name__ == '__main__':
    sample_values = ['3.14', '2.718', '1.618', '0.577']
    analyzer = NumericStringAnalyzer()
    print(f"Minimum of {sample_values}: {analyzer.get_minimum(sample_values)}")