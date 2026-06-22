class ListAnalyzer:
    MAX_VALUE_ERROR = "The list is empty"

    @staticmethod
    def get_maximum(data):
        if not data:
            raise ValueError(ListAnalyzer.MAX_VALUE_ERROR)
        return max(data)

if __name__ == '__main__':
    sample_list = [10, 5, 42, 3, 99, 21]
    maximum_value = ListAnalyzer.get_maximum(sample_list)
    print(maximum_value)