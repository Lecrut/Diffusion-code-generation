class ListAccessor:
    DEFAULT_VALUE = None

    @staticmethod
    def get_first_element(lst):
        return lst[0] if lst else ListAccessor.DEFAULT_VALUE

if __name__ == '__main__':
    sample_lists = [
        [7, 14, 21],
        [],
        ['foo', 'bar', 'baz'],
        [True, False]
    ]
    for i, lst in enumerate(sample_lists):
        print(f"First element of list {i+1}: {ListAccessor.get_first_element(lst)}")