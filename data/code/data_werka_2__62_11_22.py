class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_second(self):
        if len(self.elements) < 2:
            raise ValueError("List does not contain at least two elements.")
        return self.elements[1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    sample_list_4 = [1]

    accessor_1 = ListAccessor(sample_list_1)
    accessor_2 = ListAccessor(sample_list_2)
    accessor_3 = ListAccessor(sample_list_3)
    accessor_4 = ListAccessor(sample_list_4)

    try:
        print(f"List {sample_list_1}: {accessor_1.get_second()}")
    except ValueError as e:
        print(e)

    try:
        print(f"List {sample_list_2}: {accessor_2.get_second()}")
    except ValueError as e:
        print(e)

    try:
        print(f"List {sample_list_3}: {accessor_3.get_second()}")
    except ValueError as e:
        print(e)

    try:
        print(f"List {sample_list_4}: {accessor_4.get_second()}")
    except ValueError as e:
        print(e)