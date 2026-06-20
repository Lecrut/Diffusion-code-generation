class NestedDictAccessor:

    def __init__(self, data):
        self.data = data

    def get_nested_value(self, *keys):
        current_data = self.data
        for key in keys:
            if isinstance(current_data, dict) and key in current_data:
                current_data = current_data[key]
            else:
                return None
        return current_data
if __name__ == '__main__':
    sample_data = {'a': {'b': {'c': 1, 'd': 2}, 'e': 3}, 'f': 4}
    accessor = NestedDictAccessor(sample_data)
    print(accessor.get_nested_value('a', 'b', 'c'))
    print(accessor.get_nested_value('a', 'b', 'd'))
    print(accessor.get_nested_value('f'))
    print(accessor.get_nested_value('g'))