class ListConcatenator:
    @staticmethod
    def concatenate(list_x, list_y):
        result = list_x[:]
        result[len(result):] = list_y
        return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(ListConcatenator.concatenate(sample_list1, sample_list2))