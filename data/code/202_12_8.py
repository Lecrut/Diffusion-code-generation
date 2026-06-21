class FloatConverter:
    def convert_to_floats(self, data_list):
        return [float(item) for item in data_list]

class NumberAnalyzer:
    def __init__(self, converter=FloatConverter()):
        self.converter = converter

    def get_maximum(self, data_list):
        float_data = self.converter.convert_to_floats(data_list)
        if not float_data:
            raise ValueError("Input list cannot be empty")
        maximum = float_data[0]
        for number in float_data[1:]:
            if number > maximum:
                maximum = number
        return maximum

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_data1 = [10, 5, 20.5, "8", -3]
    sample_data2 = [-5, -1.5, -10, "3"]
    result1 = analyzer.get_maximum(sample_data1)
    print(f"Maximum of {sample_data1}: {result1}")
    result2 = analyzer.get_maximum(sample_data2)
    print(f"Maximum of {sample_data2}: {result2}")