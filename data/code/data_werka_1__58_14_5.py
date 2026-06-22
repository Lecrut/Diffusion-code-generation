class ListUtils:
    EMPTY_LIST_MESSAGE = "The list is empty."

    @staticmethod
    def get_first_element(lst):
        return lst[0] if lst else None

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    for i, lst in enumerate(sample_lists):
        first_element = ListUtils.get_first_element(lst)
        if first_element is None:
            print(f"List {i+1}: {ListUtils.EMPTY_LIST_MESSAGE}")
        else:
            print(f"First element of list {i+1}: {first_element}")