class ListConcatenator:
    @staticmethod
    def extend_list(base_list, extension):
        base_list.extend(extension)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    
    result_list = sample_list_a.copy()
    ListConcatenator.extend_list(result_list, sample_list_b)
    
    print(result_list)