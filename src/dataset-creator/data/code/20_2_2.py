def map_names_to_indices(names):
    name_to_index = {}
    for index, name in enumerate(names):
        if name not in name_to_index:
            name_to_index[name] = index
    return name_to_index
if __name__ == '__main__':
    student_names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
    result = map_names_to_indices(student_names)
    print(result)