class IterableInspector:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_first_item(self):
        return next(iter(self.iterable), None)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    inspector = IterableInspector(sample_list)
    first_item = inspector.get_first_item()
    print(first_item)

    sample_tuple = (50, 60, 70)
    tuple_inspector = IterableInspector(sample_tuple)
    first_tuple_item = tuple_inspector.get_first_item()
    print(first_tuple_item)

    sample_string = "hello"
    string_inspector = IterableInspector(sample_string)
    first_string_char = string_inspector.get_first_item()
    print(first_string_char)

    empty_list = []
    empty_inspector = IterableInspector(empty_list)
    first_empty_item = empty_inspector.get_first_item()
    print(first_empty_item)