class SafeListAccessor:
    def __init__(self, items):
        self.items = items

    def get_last_element(self):
        try:
            return self.items[-1]
        except IndexError:
            raise ValueError("The list is empty.")

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    accessor_1 = SafeListAccessor(sample_list_1)
    print(accessor_1.get_last_element())

    sample_list_2 = []
    accessor_2 = SafeListAccessor(sample_list_2)
    try:
        print(accessor_2.get_last_element())
    except ValueError as e:
        print(e)

    sample_list_3 = ['a', 'b', 'c']
    accessor_3 = SafeListAccessor(sample_list_3)
    print(accessor_3.get_last_element())

    sample_list_4 = [True, False, True]
    accessor_4 = SafeListAccessor(sample_list_4)
    print(accessor_4.get_last_element())