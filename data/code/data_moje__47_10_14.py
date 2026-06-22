def calculate_mean():
    scores = [85, 90, 78, 92, 88]
    total = 0
    count = 0
    for score in scores:
        if not isinstance(score, (int, float)):
            raise TypeError("All scores must be numeric")
        total += score
        count += 1
    if count == 0:
        return 0.0
    return float(total / count)

if __name__ == '__main__':
    result = calculate_mean()
    print(result)