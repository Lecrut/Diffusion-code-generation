def find_max_valid_score(scores: tuple) -> int | None:
    max_val = None
    for score in scores:
        if isinstance(score, int) and (not isinstance(score, bool)):
            if max_val is None or score > max_val:
                max_val = score
    return max_val
if __name__ == '__main__':
    scores = (85, 'invalid', 92, 7, 0, -5, 100, 'missing', 45)
    result = find_max_valid_score(scores)
    print(result)