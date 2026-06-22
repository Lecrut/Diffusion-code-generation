def calculate_average():
    scores = [88, 92, 79, 93, 85, 90, 88, 91, 87, 95]
    total = sum(score for score in scores)
    count = len(scores)
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    result = calculate_average()
    print(result)