class ListExtender:
    @staticmethod
    def extend_with_last_element(lst, n):
        lst.extend([lst[-1]] * n)
        return lst

if __name__ == '__main__':
    sample_list = [4, 5, 6]
    num_copies = 2
    result = ListExtender.extend_with_last_element(sample_list, num_copies)
    print(result)