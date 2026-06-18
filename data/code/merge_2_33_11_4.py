def check_name_exists(names: list[str], target: str) -> bool:
    if not names:
        return False
    name_set = set(names)
    def lookup(name: str) -> bool:
        return name in name_set
    result = lookup(target)
    del name_set, lookup
    return result
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    target_name = "Bob"
    exists = check_name_exists(sample_names, target_name)
    print(exists)