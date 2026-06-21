from functools import cmp_to_key

class Sorter:
    DEFAULT_KEY = lambda x: x

    @staticmethod
    def _validate_key_function(key_function):
        if not callable(key_function):
            raise ValueError("Key function must be callable")

    def sort_data(self, data_list, key_function=DEFAULT_KEY):
        self._validate_key_function(key_function)
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    custom_sort_key = lambda x: len(str(x))
    sorted_data = sorter.sort_data(sample_data, custom_sort_key)
    print(sorted_data)