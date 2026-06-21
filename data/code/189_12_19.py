def remove_by_index(data_list, index):
    if not isinstance(data_list, list) or not isinstance(index, int):
        raise ValueError('Invalid input: data_list must be a list and index must be an integer')
    if index < 0 or index >= len(data_list):
        print(f'Index {index} is out of range. No item removed.')
        return
    del data_list[index]
    print(f'Item at index {index} removed.')
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    remove_by_index(my_list, 2)
    print('Updated list:', my_list)
    my_list_2 = ['a', 'b', 'c', 'd']
    remove_by_index(my_list_2, 0)
    print('Updated list:', my_list_2)
    my_list_3 = [10, 20, 30]
    remove_by_index(my_list_3, 5)