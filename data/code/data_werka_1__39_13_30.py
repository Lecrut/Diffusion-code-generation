def extract_substrings(s, start, end):
    START_CHAR = start
    END_CHAR = end
    substrings = []
    start_indices = [i for i, char in enumerate(s) if char == START_CHAR]
    end_indices = [j for j, char in enumerate(s) if char == END_CHAR]
    for s_index in start_indices:
        for e_index in end_indices:
            if s_index < e_index:
                substrings.append(s[s_index:e_index + 1])
    return substrings

if __name__ == '__main__':
    target_string = "xyzabcdeaxyz"
    start_point = 'a'
    end_point = 'e'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)