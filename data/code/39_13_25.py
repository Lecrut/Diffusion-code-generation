def extract_substrings(s, start, end):
    if not isinstance(s, str) or not isinstance(start, str) or not isinstance(end, str):
        raise ValueError("All inputs must be strings.")
    if len(start) != 1 or len(end) != 1:
        raise ValueError("Start and end points must be single characters.")

    start_indices = [i for i, char in enumerate(s) if char == start]
    end_indices = [j for j, char in enumerate(s) if char == end]

    substrings = []
    for s_index in start_indices:
        for e_index in end_indices:
            if s_index < e_index:
                substrings.append(s[s_index:e_index + 1])
    return substrings

if __name__ == '__main__':
    target_string = "hello world"
    start_point = 'h'
    end_point = 'd'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)