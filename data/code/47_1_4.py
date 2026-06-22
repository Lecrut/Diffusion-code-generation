import statistics

def compute_mean_score():
    scores = [85, 90, 78, 92, 88, 76, 95, 89, 91, 87]
    return statistics.mean(scores)

if __name__ == '__main__':
    result = compute_mean_score()
    print(result)