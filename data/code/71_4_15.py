class MiddleElementFinder:
    FOUND_INDEX_KEY = 'index'
    FOUND_VALUE_KEY = 'value'

    @staticmethod
    def _validate_non_empty_list(data):
        if not data:
            raise ValueError("List must not be empty")
        return data

    def find_middle(self, numbers):
        validated_list = self._validate_non_empty_list(numbers)
        count = len(validated_list)
        mid_idx = count // 2
        return {
            self.FOUND_INDEX_KEY: mid_idx,
            self.FOUND_VALUE_KEY: validated_list[mid_idx]
        }

if __name__ == '__main__':
    finder = MiddleElementFinder()
    sample_data = [7, 14, 21, 28, 35]
    result = finder.find_middle(sample_data)
    print(result)