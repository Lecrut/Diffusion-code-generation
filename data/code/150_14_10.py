class ListModifier:
    def __init__(self, initial_list):
        self.data = initial_list

    def remove_first_occurrence(self, item_to_remove):
        try:
            index = self.data.index(item_to_remove)
            del self.data[index]
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    modifier1 = ListModifier([1, 2, 3, 4, 5])
    item1 = 3
    success1 = modifier1.remove_first_occurrence(item1)
    print(f"List: {modifier1.data}, Item to remove: {item1}, Success: {success1}")
    
    modifier2 = ListModifier([10, 20, 30])
    item2 = 99
    success2 = modifier2.remove_first_occurrence(item2)
    print(f"List: {modifier2.data}, Item to remove: {item2}, Success: {success2}")
    
    modifier3 = ListModifier(['a', 'b', 'c'])
    item3 = 'd'
    success3 = modifier3.remove_first_occurrence(item3)
    print(f"List: {modifier3.data}, Item to remove: {item3}, Success: {success3}")