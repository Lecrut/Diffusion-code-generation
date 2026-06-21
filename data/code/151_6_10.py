class ListExtender:
    def extend_list_in_place(self, list1, list2):
        list1.extend(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    extender = ListExtender()
    extender.extend_list_in_place(sample_list1, sample_list2)
    print(sample_list1)