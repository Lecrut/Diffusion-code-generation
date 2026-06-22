class MinFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def find_min_value(nested_list):
        current_min = MinFinder.MIN_VALUE
        for item in nested_list:
            if isinstance(item, list):
                sub_min = MinFinder.find_min_value(item)
                if sub_min < current_min:
                    current_min = sub_min
            elif item < current_min:
                current_min = item
        return current_min

if __name__ == '__main__':
    sample_data = [[10, 2], [3, [4, 5]], 6, 1]
    min_value = MinFinder.find_min_value(sample_data)
    print(min_value)