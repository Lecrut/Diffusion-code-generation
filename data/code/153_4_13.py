def check_presence(target_list: list, master_list: list) -> bool:
    try:
        master_set = set(master_list)
        for item in target_list:
            if not isinstance(item, type(next(iter(master_set)))):
                raise ValueError("All items in target_list must be of the same type as elements in master_list")
            if item in master_set:
                return True
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    result = check_presence(target, master)
    print(result)