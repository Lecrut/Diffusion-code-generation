class NumericStringAnalyzer:
    @staticmethod
    def get_minimum_value(lst):
        if not lst:
            raise ValueError("List cannot be empty")
        return min(float(x) for x in lst)

if __name__ == '__main__':
    sample_values = ['3.14', '2.718', '1.618', '0.577']
    print(f"Minimum value: {NumericStringAnalyzer.get_minimum_value(sample_values)}")