from typing import List, Union

class DataAnalyzer:
    NUMERIC_TYPES = (int, float)
    
    @staticmethod
    def clean_and_convert(data: List[Union[int, float, str, None]]) -> List[Union[int, float]]:
        return [
            int(x) if isinstance(x, str) and x.isdigit() else float(x)
            for x in data
            if isinstance(x, DataAnalyzer.NUMERIC_TYPES) or (isinstance(x, str) and x.replace('.', '', 1).isdigit())
        ]
    
    @staticmethod
    def is_numeric(value: Union[int, float, str]) -> bool:
        return isinstance(value, DataAnalyzer.NUMERIC_TYPES) or \
               (isinstance(value, str) and value.replace('.', '', 1).isdigit())

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5']
    cleaned_data = DataAnalyzer.clean_and_convert(sample_data)
    print(cleaned_data)