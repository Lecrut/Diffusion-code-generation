class ListConcatenator:
    @staticmethod
    def extend_list(list1, list2):
        result = list1.copy()
        result.extend(list2)
        return result

if __name__ == '__main__':
    sample_list1 = [i for i in range(5000)]
    sample_list2 = [i for i in range(5000, 10000)]
    concatenated_result = ListConcatenator.extend_list(sample_list1, sample_list2)
    print(concatenated_result[:5])