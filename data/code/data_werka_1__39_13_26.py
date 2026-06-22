def extract_substrings(s, start_point, end_point):
    return [s[i:j] for i in range(len(s)) if s.startswith(start_point, i) 
            for j in range(i + len(start_point), len(s) + 1) if s.endswith(end_point, j)]

if __name__ == '__main__':
    target_string = "This is a test string with multiple start and end points."
    start = "start"
    end = "points"
    result = extract_substrings(target_string, start, end)
    print(result)