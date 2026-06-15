def name_to_index_map(names):
    name_to_index = {}
    for index, name in enumerate(names):
        if name not in name_to_index:
            name_to_index[name] = index
    return name_to_index
if __name__ == '__main__':
    student_names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
    result = name_to_index_map(student_names)
    print(result)