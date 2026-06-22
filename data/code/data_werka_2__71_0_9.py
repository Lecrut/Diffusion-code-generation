class MiddleElementFinder:
    _STEP = 2

    @staticmethod
    def _get_middle_index(length):
        return length // 2

    @classmethod
    def find_middle_element(cls, data):
        if not data:
            raise ValueError("List must not be empty")
        length = len(data)
        mid_idx = cls._get_middle_index(length)
        start = mid_idx - (1 if length % 2 == 0 else 0)
        end = mid_idx + 1
        slice_result = data[start:end]
        if length % 2 != 0:
            return slice_result[0]
        return (slice_result[0] + slice_result[1]) / cls._STEP

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = MiddleElementFinder.find_middle_element(sample_list)
    print(result)