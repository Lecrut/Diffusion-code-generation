def find_largest_int(scores):
    largest = None
    for score in scores:
        if isinstance(score, int) and not isinstance(score, bool):
            if largest is None or score > largest:
                largest = score
    return largest

if __name__ == '__main__':
    scores = (10, 20.5, 30, "40", 15, -5, 45.0, 35, 25)
    result = find_largest_int(scores)
    print(result)