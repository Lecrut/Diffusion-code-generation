import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    sample_scores = [85, 92, 78, 90, 88]
    print(calculate_mean(sample_scores))