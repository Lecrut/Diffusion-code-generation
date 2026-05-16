def unique_union(list_a: list[str], list_b: list[str]) -> list[str]:
    combined_set = set(list_a)
    combined_set.update(list_b)
    return list(combined_set)
if __name__ == '__main__':
    list_a_sample = ["apple", "banana", "cherry", "apple"]
    list_b_sample = ["banana", "date", "apple", "fig"]
    result = unique_union(list_a_sample, list_b_sample)
    print(result)