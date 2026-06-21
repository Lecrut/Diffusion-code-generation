class ListConcatenator:
    def concatenate(self, list1: list, list2: list) -> list:
        if isinstance(list1, list) and isinstance(list2, list):
            return list1 + list2
        else:
            raise ValueError("Both inputs must be lists")

if __name__ == '__main__':
    concat_instance = ListConcatenator()
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concat_instance.concatenate(sample_list1, sample_list2)
    print(result)