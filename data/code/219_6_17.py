class NestedListProcessor:

    @staticmethod
    def flatten_and_find_max(nested_list):
        flat_list = [item for sublist in nested_list for item in sublist]
        return max(flat_list)
if __name__ == '__main__':
    sample_list = [[3, 5], [1, 2], [4]]
    result = NestedListProcessor.flatten_and_find_max(sample_list)
    print(result)
    sample_list_2 = [[10, 20, 30], [5, 15], [7, 8, 9, 100]]
    result_2 = NestedListProcessor.flatten_and_find_max(sample_list_2)
    print(result_2)