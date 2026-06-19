class IterableAnalyzer:
    DEFAULT_VALUE = None

    @staticmethod
    def get_first_item(iterable):
        return next(iter(iterable), IterableAnalyzer.DEFAULT_VALUE)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    first_value = IterableAnalyzer.get_first_item(sample_list)
    print(first_value)

    empty_list = []
    first_value_empty = IterableAnalyzer.get_first_item(empty_list)
    print(first_value_empty)

    sample_tuple = (5, 6, 7)
    first_value_tuple = IterableAnalyzer.get_first_item(sample_tuple)
    print(first_value_tuple)

    sample_string = "hello"
    first_value_string = IterableAnalyzer.get_first_item(sample_string)
    print(first_value_string)