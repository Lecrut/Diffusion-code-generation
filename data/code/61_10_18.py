def get_list_element(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return None

class ListElementRetriever:
    def __init__(self, data_list):
        self.data_list = data_list

    def retrieve(self, index):
        return get_list_element(self.data_list, index)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index_high = 5
    invalid_index_low = -1

    retriever = ListElementRetriever(sample_list)
    
    result_valid = retriever.retrieve(valid_index)
    result_invalid_high = retriever.retrieve(invalid_index_high)
    result_invalid_low = retriever.retrieve(invalid_index_low)

    print(f"List: {sample_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Attempted access at index {invalid_index_high}: {result_invalid_high}")
    print(f"Attempted access at index {invalid_index_low}: {result_invalid_low}")