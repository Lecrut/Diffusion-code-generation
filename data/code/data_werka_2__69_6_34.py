class SublistExtractor:
    def __init__(self, larger_list):
        if not isinstance(larger_list, list):
            raise ValueError("The first argument must be a list.")
        self.larger_list = larger_list

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise ValueError("Start and end indices must be integers.")
        if start_index < 0 or end_index >= len(self.larger_list):
            raise IndexError("Start index out of range.")
        if start_index > end_index:
            raise ValueError("Start index cannot be greater than end index.")
        return self.larger_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    extractor = SublistExtractor(sample_data)
    
    starting_point = 0
    ending_point = 2
    result_sublist1 = extractor.get_sublist(starting_point, ending_point)
    print(result_sublist1)

    starting_point2 = 1
    ending_point2 = 4
    result_sublist2 = extractor.get_sublist(starting_point2, ending_point2)
    print(result_sublist2)