class ListElementRetriever:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        try:
            element = self.data_list[index]
            return element
        except IndexError:
            return "Error: Index out of bounds"

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListElementRetriever(sample_list)
    valid_index = 2
    invalid_index_high = 5
    invalid_index_low = -1

    result_valid = retriever.get_element(valid_index)
    result_invalid_high = retriever.get_element(invalid_index_high)
    result_invalid_low = retriever.get_element(invalid_index_low)

    print(f"List: {sample_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Attempted access at index {invalid_index_high}: {result_invalid_high}")
    print(f"Attempted access at index {invalid_index_low}: {result_invalid_low}")