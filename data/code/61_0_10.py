class ListElementRetriever:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        try:
            return self.data_list[index]
        except IndexError:
            return "Index out of bounds"

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    retriever = ListElementRetriever(sample_data)
    
    valid_index = 2
    invalid_index = 7
    
    result_valid = retriever.get_element(valid_index)
    result_invalid = retriever.get_element(invalid_index)
    
    print(f"List: {sample_data}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Element at index {invalid_index}: {result_invalid}")