def find_largest_integer(scores):
    filtered = [s for s in scores if isinstance(s, int) and not isinstance(s, bool)]
    if not filtered:
        return None
    max_val = filtered[0]
    for val in filtered[1:]:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    sample_scores = (85, 90.5, "A", 78, None, 92, 88.0, 95, True, 70)
    result = find_largest_integer(sample_scores)
    print(result)