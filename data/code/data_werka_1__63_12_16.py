class IterableInspector:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_first_item(self):
        return next(iter(self.iterable), None)

if __name__ == '__main__':
    sample_list = [7, 8, 9]
    sample_tuple = (10, 11, 12)
    sample_string = "world"
    empty_dict = {}

    inspector_list = IterableInspector(sample_list)
    first_list_item = inspector_list.get_first_item()
    print(first_list_item)

    inspector_tuple = IterableInspector(sample_tuple)
    first_tuple_item = inspector_tuple.get_first_item()
    print(first_tuple_item)

    inspector_string = IterableInspector(sample_string)
    first_string_char = inspector_string.get_first_item()
    print(first_string_char)

    inspector_empty_dict = IterableInspector(empty_dict)
    first_empty_dict_item = inspector_empty_dict.get_first_item()
    print(first_empty_dict_item)