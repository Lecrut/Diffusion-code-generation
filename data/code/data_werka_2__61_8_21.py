class ListManager:
    def __init__(self, initial_list):
        self.lst = initial_list

    def pop_element(self, index):
        try:
            return self.lst.pop(index)
        except IndexError:
            print("Index out of range")
            return None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP = 2
    manager = ListManager(SAMPLE_LIST)
    popped_element = manager.pop_element(INDEX_TO_POP)
    print("Popped element:", popped_element)
    print("List after popping:", manager.lst)