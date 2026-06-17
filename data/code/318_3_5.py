def find_different_length_adjacent_pairs(string_list):
    result = []
    n = len(string_list)
    for i in range(n - 1):
        if len(string_list[i]) != len(string_list[i+1]):
            result.append((string_list[i], string_list[i+1]))
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "grapefruit", "orange"]
    output = find_different_length_adjacent_pairs(sample_list)
    for s1, s2 in output:
        print(f"Pair: ('{s1}', '{s2}')")