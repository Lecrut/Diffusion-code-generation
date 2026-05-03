if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    index_to_pop = 2
    if 0 <= index_to_pop < len(my_list):
        removed_element = my_list.pop(index_to_pop)
        print(f"Element removed: {removed_element}")
        print(f"List after pop: {my_list}")
    else:
        print("Error: Index is out of bounds.")