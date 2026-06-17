def find_different_length_pairs(list_of_strings):
    result = []
    n = len(list_of_strings)
    for i in range(n - 1):
        if len(list_of_strings[i]) != len(list_of_strings[i+1]):
            result.append((list_of_strings[i], list_of_strings[i+1]))
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "grapefruit", "orange"]
    output = find_different_length_pairs(sample_list)
    for s1, s2 in output:
        print(f"('{s1}', '{s2}')")