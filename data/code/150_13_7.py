def remove_target(data, target):
    return [item for item in data if item != target]

if __name__ == '__main__':
    initial_list = [1, 2, 3, 4, 2, 5, 2, 6]
    target_value = 2
    print("Initial list:", initial_list)
    modified_list = remove_target(initial_list, target_value)
    print("List after removing instances of", target_value, ":", modified_list)