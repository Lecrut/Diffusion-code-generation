class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50]
    
    def __init__(self, data=None):
        self.data = data if data is not None else ListAccessor.DEFAULT_LIST
    
    @staticmethod
    def validate_index(index, length):
        if index < 0 or index >= length:
            raise ValueError("Index out of bounds")
    
    def get_element(self, index):
        ListAccessor.validate_index(index, len(self.data))
        return self.data[index]

if __name__ == '__main__':
    sample_list = [150, 250, 350, 450, 550]
    index_to_retrieve = 1
    accessor = ListAccessor(sample_list)
    try:
        element = accessor.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)