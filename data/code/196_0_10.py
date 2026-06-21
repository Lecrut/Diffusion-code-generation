class ListConcatenator:
    @staticmethod
    def concatenate(list1, list2):
        result = list1.copy()
        result.extend(list2)
        return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(1000000)]
    sample_list2 = [i for i in range(1000000, 2000000)]
    concatenated_result = ListConcatenator.concatenate(sample_list1, sample_list2)
    print(concatenated_result[:5])