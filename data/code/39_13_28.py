def extract_substrings(s, start, end):
    if not s or start not in s or end not in s:
        return []
    
    result = []
    start_indices = [i for i, char in enumerate(s) if char == start]
    end_indices = [j for j, char in enumerate(s) if char == end]
    
    for s_index in start_indices:
        for e_index in end_indices:
            if s_index < e_index:
                result.append(s[s_index:e_index + 1])
    
    return result

if __name__ == '__main__':
    target_string = "abcdeabc"
    start_point = 'a'
    end_point = 'e'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)