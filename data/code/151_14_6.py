class ListConcatenator:
    @staticmethod
    def concatenate(list1, list2):
        if isinstance(list1, list) and isinstance(list2, list):
            return list1 + list2
        else:
            raise ValueError("Both inputs must be lists")

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = ListConcatenator.concatenate(sample_list1, sample_list2)
    print(result)