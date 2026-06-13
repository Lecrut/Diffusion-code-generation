class MutableListManager:
    def __init__(self, initial_list):
        self._data = list(initial_list)
    def remove_by_index(self, index):
        if not (0 <= index < len(self._data)):
            raise IndexError("Index out of bounds")
        del self._data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manager = MutableListManager(sample_list)
    print("Initial list:", sample_list)
    try:
        manager.remove_by_index(2)
        print("After removing index 2:", manager._data)
    except IndexError as e:
        print("Error:", e)
    try:
        manager.remove_by_index(5)
    except IndexError as e:
        print("Caught expected error for index 5:", e)
    try:
        manager.remove_by_index(-1)
    except IndexError as e:
        print("Caught expected error for index -1:", e)
    sample_list_2 = ['a', 'b', 'c']
    manager_2 = MutableListManager(sample_list_2)
    print("\nInitial list 2:", sample_list_2)
    try:
        manager_2.remove_by_index(0)
        print("After removing index 0:", manager_2._data)
    except IndexError as e:
        print("Error:", e)