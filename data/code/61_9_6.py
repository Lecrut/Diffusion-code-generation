class ListManager:

    def __init__(self, initial_list):
        self.list = initial_list

    def safe_pop(self, index):
        try:
            return self.list.pop(index)
        except IndexError:
            print('Error: Index out of bounds.')
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manager = ListManager(sample_list)
    index_to_pop = 2
    popped_element = manager.safe_pop(index_to_pop)
    print('Popped element:', popped_element)
    print('Remaining list:', manager.list)
    invalid_index = 10
    result = manager.safe_pop(invalid_index)
    if result is not None:
        print(f'Element removed: {result}')
    else:
        print('Failed to remove element.')