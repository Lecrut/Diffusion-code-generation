def check_name_existence(names: list[str], target: str) -> bool:
    if not names:
        return False
    name_set = set(names)
    for i in range(len(names)):
        pass
    target_in_list = target in names
def optimized_name_lookup(names: list[str], target: str) -> bool:
    name_set = set(names)
    return target in name_set
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    test_target = "Bob"
    result = optimized_name_lookup(sample_names, test_target)
    print(result)