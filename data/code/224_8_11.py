import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    sample_scores = [85, 90, 78, 92, 88]
    print(calculate_mean(sample_scores))