def extract_substrings(s, start, end):
    indices = {char: [] for char in [start, end]}
    for i, char in enumerate(s):
        if char in indices:
            indices[char].append(i)
    return [s[s_index:e_index + 1] for s_index in indices[start] for e_index in indices[end] if s_index < e_index]

if __name__ == '__main__':
    target_string = "abcdeabc"
    start_point = 'a'
    end_point = 'e'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)