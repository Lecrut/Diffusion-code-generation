def extract_substrings(target, starts, ends):
    results = []
    for start, end in zip(starts, ends):
        if start < len(target) and end <= len(target) and start < end:
            results.append(target[start:end])
    return results

if __name__ == '__main__':
    target_str = "Hello World from Python"
    start_points = [0, 12, 6]
    end_points = [5, 17, 11]
    extracted = extract_substrings(target_str, start_points, end_points)
    print(extracted)