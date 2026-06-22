def find_max_valid_int(scores):
    max_val = None
    for score in scores:
        if isinstance(score, int) and not isinstance(score, bool):
            if max_val is None or score > max_val:
                max_val = score
    return max_val

if __name__ == '__main__':
    sample_data = (10, "A", 3.14, -5, 42, True, 15, None, 100, "88")
    result = find_max_valid_int(sample_data)
    print(result)