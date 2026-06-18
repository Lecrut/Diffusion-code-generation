def check_name_existence(names: list[str], target: str) -> bool:
    if not names:
        return False
    name_set = set(names)
    def lookup(name: str) -> bool:
        return name in name_set
    return lookup(target)
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    target_name = "Alice"
    result = check_name_existence(sample_names, target_name)
    print(result)