class ComparisonTool:
    @staticmethod
    def check_greater(a, b):
        return a > b

if __name__ == '__main__':
    sample_values = [(10, 5), (5, 10), (7.5, 7.5), (200, 199), (-1, -5)]
    for value1, value2 in sample_values:
        result = ComparisonTool.check_greater(value1, value2)
        print(f"{value1} > {value2}: {result}")