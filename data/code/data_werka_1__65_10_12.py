class ListAccessor:
    def __init__(self, my_list):
        self.my_list = my_list

    def get_sublist(self, start_index, end_index):
        return self.my_list[start_index:end_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print("Original list:", sample_list)
    sublist = accessor.get_sublist(2, 5)
    print("Sublist from index 2 to 4:", sublist)