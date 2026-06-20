class DataAnalyzer:
    NUMERIC_TYPES = (int, float)

    @staticmethod
    def is_numeric(value):
        return isinstance(value, DataAnalyzer.NUMERIC_TYPES) or \
               isinstance(value, str) and value.replace('.', '', 1).isdigit()

    @staticmethod
    def clean_and_convert(data):
        cleaned_data = []
        for item in data:
            if DataAnalyzer.is_numeric(item):
                try:
                    if '.' in str(item):
                        cleaned_data.append(float(item))
                    else:
                        cleaned_data.append(int(item))
                except ValueError:
                    continue
        return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    analyzer = DataAnalyzer()
    print(analyzer.clean_and_convert(sample_data))