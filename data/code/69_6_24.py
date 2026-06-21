class SublistExtractor:
    @staticmethod
    def validate_input(larger_list, start_index, end_index):
        if not isinstance(larger_list, list):
            raise ValueError("The first argument must be a list.")
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise ValueError("Start and end indices must be integers.")
        if start_index < 0 or end_index >= len(larger_list):
            raise IndexError("Start index out of range.")
        if start_index > end_index:
            raise ValueError("Start index cannot be greater than end index.")

    @staticmethod
    def get_sublist(larger_list, start_index, end_index):
        SublistExtractor.validate_input(larger_list, start_index, end_index)
        return larger_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    starting_point = 1
    ending_point = 4
    result_sublist = SublistExtractor.get_sublist(sample_data, starting_point, ending_point)
    print(result_sublist)