class SafeListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_second_element(self):
        return self.lst[1] if len(self.lst) > 1 else None

if __name__ == '__main__':
    sample_list_1 = [15, 25, 35]
    sample_list_2 = [99]
    sample_list_3 = []

    accessor_1 = SafeListAccessor(sample_list_1)
    accessor_2 = SafeListAccessor(sample_list_2)
    accessor_3 = SafeListAccessor(sample_list_3)

    print(accessor_1.get_second_element())
    print(accessor_2.get_second_element())
    print(accessor_3.get_second_element())