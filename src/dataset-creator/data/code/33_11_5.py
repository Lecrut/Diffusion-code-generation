def exists(name_list: list, target_name) -> bool:
    return target_name in name_list
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie"]
    print(exists(names, "David"))