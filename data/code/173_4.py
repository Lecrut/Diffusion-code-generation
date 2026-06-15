def group_strings(string_list):
    grouped = {}
    for s in string_list:
        if s:
            first_letter = s[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(s)
    return grouped
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apricot", "cat", "ball", "ant"]
    result = group_strings(sample_list)
    print(result)