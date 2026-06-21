def check_presence(target_list: list[int], master_list: list[int]) -> bool:
    if not all(isinstance(item, int) for item in target_list + master_list):
        raise ValueError("Both target_list and master_list must contain only integers.")
    
    master_set = set(master_list)
    return any(item in master_set for item in target_list)

if __name__ == '__main__':
    target = [1, 5, 9, 12]
    master = list(range(1, 100))
    result = check_presence(target, master)
    print(result)