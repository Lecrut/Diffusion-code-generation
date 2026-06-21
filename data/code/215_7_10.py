class NestedListMax:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def flatten(self):
        flat_list = []
        for sublist in self.nested_list:
            if isinstance(sublist, list):
                flat_list.extend(self.flatten(sublist))
            else:
                flat_list.append(sublist)
        return flat_list

    def find_largest(self):
        flat_list = self.flatten()
        largest = max(flat_list)
        return largest

if __name__ == '__main__':
    nested_list_instance = NestedListMax([[1, 5], [3, 2], [9, 4]])
    print(f"Largest in the nested list: {nested_list_instance.find_largest()}")