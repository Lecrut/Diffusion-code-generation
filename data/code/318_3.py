def find_adjacent_different_lengths(string_list):
    result = []
    for i in range(len(string_list) - 1):
        current_string = string_list[i]
        next_string = string_list[i+1]
        if len(current_string) != len(next_string):
            result.append((current_string, next_string))
    return result
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "grapefruit", "orange"]
    output = find_adjacent_different_lengths(sample_list)
    for s1, s2 in output:
        print(f"('{s1}', '{s2}')")