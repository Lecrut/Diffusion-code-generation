class SafeIterableHandler:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_first_element(self):
        try:
            return next(iter(self.iterable))
        except (TypeError, StopIteration):
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (40, 50, 60)
    sample_string = "hello"
    sample_dict = {'a': 1, 'b': 2}
    sample_set = {70, 80, 90}
    sample_empty_list = []

    handler_list = SafeIterableHandler(sample_list)
    handler_tuple = SafeIterableHandler(sample_tuple)
    handler_string = SafeIterableHandler(sample_string)
    handler_dict = SafeIterableHandler(sample_dict)
    handler_set = SafeIterableHandler(sample_set)
    handler_empty_list = SafeIterableHandler(sample_empty_list)

    print(handler_list.get_first_element())
    print(handler_tuple.get_first_element())
    print(handler_string.get_first_element())
    print(handler_dict.get_first_element())  # This will print None
    print(handler_set.get_first_element())   # This will print None
    print(handler_empty_list.get_first_element())  # This will print None