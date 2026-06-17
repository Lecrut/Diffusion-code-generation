def check_name_existence(names: list[str], target: str) -> bool:
    name_set = set(names)
    return target in name_set
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    test_target = "Bob"
    result = check_name_existence(sample_names, test_target)
    print(result)