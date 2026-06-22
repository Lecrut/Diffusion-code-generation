class SafeAccess:
    @staticmethod
    def get_element(sequence, index):
        try:
            return sequence[index]
        except IndexError:
            return None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    my_tuple = (1, 2, 3, 4, 5)
    index_to_find = 2
    list_element = SafeAccess.get_element(my_list, index_to_find)
    tuple_element = SafeAccess.get_element(my_tuple, index_to_find)
    print(f"Element at index {index_to_find} in the list: {list_element}")
    print(f"Element at index {index_to_find} in the tuple: {tuple_element}")