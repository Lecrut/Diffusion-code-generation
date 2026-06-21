class ListConcatenator:
    def concatenate(self, list1, list2):
        return list1 + list2

if __name__ == '__main__':
    concatenator = ListConcatenator()
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenator.concatenate(sample_list1, sample_list2)
    print(result)