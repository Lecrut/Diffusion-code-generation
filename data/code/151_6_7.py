class ListExtender:
    @staticmethod
    def extend_list_in_place(list1, list2):
        list1.extend(list2)

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    ListExtender.extend_list_in_place(sample_list1, sample_list2)
    print(sample_list1)