class ListProcessor:
    def __init__(self, initial_list):
        self.lst = initial_list
    
    def pop_element(self, index):
        try:
            return self.lst.pop(index)
        except IndexError:
            raise ValueError("Index out of range")

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP_1 = 2
    INDEX_TO_POP_2 = 4

    processor = ListProcessor(SAMPLE_LIST)
    
    try:
        popped_element_1 = processor.pop_element(INDEX_TO_POP_1)
        print(f"Popped element at index {INDEX_TO_POP_1}: {popped_element_1}")
        print(f"List after popping: {processor.lst}")

        popped_element_2 = processor.pop_element(INDEX_TO_POP_2)
        print(f"Popped element at index {INDEX_TO_POP_2}: {popped_element_2}")
        print(f"List after popping: {processor.lst}")
    except ValueError as e:
        print(e)