class ListModifier:
    def __init__(self, initial_list):
        self.data = initial_list.copy()

    def remove_by_index(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
        else:
            print(f"Index out of range: {index}")

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6]
    modifier = ListModifier(my_list)
    modifier.remove_by_index(2)
    print("List after removing index 2:", modifier.data)
    
    modifier.remove_by_index(0)
    print("List after removing index 0:", modifier.data)

    modifier.remove_by_index(10)
    print("List after attempting to remove out-of-range index 10:")