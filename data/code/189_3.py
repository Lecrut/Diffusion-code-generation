if __name__ == '__main__':
    data = [1, 2, 3, 4, 2, 5, 2, 6]
    element_to_remove = 2
    new_list = [item for item in data if item != element_to_remove]
    print(new_list)