class ListHandler:
    DEFAULT_LIST = [10, 20, 30, 40, 50]
    
    @staticmethod
    def pop_element(lst, index):
        try:
            return lst.pop(index)
        except IndexError:
            raise ValueError("Index out of range")

if __name__ == '__main__':
    sample_list = ListHandler.DEFAULT_LIST.copy()
    index_to_pop = 2
    
    try:
        popped_element = ListHandler.pop_element(sample_list, index_to_pop)
        print("Popped element:", popped_element)
        print("List after popping:", sample_list)
    except ValueError as e:
        print(e)