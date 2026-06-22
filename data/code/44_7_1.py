def calculate_average(scores):
    return sum(scores) / len(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 95, 88]
    result = calculate_average(sample_scores)
    print(result)