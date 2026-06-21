class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_first_middle_last(self):
        if not self.data:
            return ()
        
        first_element = self.data[0]
        last_element = self.data[-1]
        middle_index = len(self.data) // 2
        middle_element = self.data[middle_index]
        
        return (first_element, middle_element, last_element)

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11, 13]
    accessor = ListAccessor(sample_list)
    result = accessor.get_first_middle_last()
    print(result)