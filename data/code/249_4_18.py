class ListAnalyzer:
    @staticmethod
    def get_maximum(data):
        if not data:
            raise ValueError("The list is empty")
        return max(item for item in data)

if __name__ == '__main__':
    sample_list = [10, 5, 42, 3, 99, 21]
    maximum_value = ListAnalyzer.get_maximum(sample_list)
    print(maximum_value)