def name_to_index(names):
    result = {}
    for index, name in enumerate(names):
        if name not in result:
            result[name] = index
    return result
if __name__ == '__main__':
    student_names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
    index_map = name_to_index(student_names)
    print(index_map)