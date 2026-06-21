def calculate_average(scores):
    return sum(scores.values()) / len(scores) if scores else 0

if __name__ == '__main__':
    sample_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    print(calculate_average(sample_scores))