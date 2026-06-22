class ListValidator:
    @staticmethod
    def are_all_ints(lst):
        return all(isinstance(x, int) for x in lst)

if __name__ == '__main__':
    sample_list = [10, 5, 22, 8, 30, 15, 7]
    print(ListValidator.are_all_ints(sample_list))
    
    sample_list_with_non_int = [1, 2, '3', 4, 5]
    print(ListValidator.are_all_ints(sample_list_with_non_int))