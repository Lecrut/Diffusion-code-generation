def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
    average = calculate_average(sample_scores)
    print(average)