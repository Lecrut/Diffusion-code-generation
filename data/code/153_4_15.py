def check_presence(target_list: list, master_list: list) -> bool:
    if not isinstance(target_list, list) or not isinstance(master_list, list):
        raise ValueError("Both target_list and master_list must be of type list.")
    
    if not all(isinstance(item, (int, float)) for item in target_list + master_list):
        raise ValueError("All elements in both lists must be integers or floats.")
    
    master_set = set(master_list)
    return any(item in master_set for item in target_list)

if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    result = check_presence(target, master)
    print(result)