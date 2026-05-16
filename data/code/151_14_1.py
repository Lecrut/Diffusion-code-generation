def unique_strings_union(list_a: list[str], list_b: list[str]) -> list[str]:
    return list(set(list_a) | set(list_b))
if __name__ == '__main__':
    list_a_sample = ["apple", "banana", "cherry", "apple", "date"]
    list_b_sample = ["banana", "elderberry", "fig", "apple", "grape"]
    result = unique_strings_union(list_a_sample, list_b_sample)
    print(result)