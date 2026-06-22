class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_second(self):
        if len(self.data) > 1:
            return self.data[1]
        else:
            return None

if __name__ == '__main__':
    sample_list_1 = [100, 200, 300, 400]
    sample_list_2 = [50]
    sample_list_3 = []
    sample_list_4 = [1]

    accessor_1 = ListAccessor(sample_list_1)
    accessor_2 = ListAccessor(sample_list_2)
    accessor_3 = ListAccessor(sample_list_3)
    accessor_4 = ListAccessor(sample_list_4)

    print(f"List {sample_list_1}: {accessor_1.get_second()}")
    print(f"List {sample_list_2}: {accessor_2.get_second()}")
    print(f"List {sample_list_3}: {accessor_3.get_second()}")
    print(f"List {sample_list_4}: {accessor_4.get_second()}")