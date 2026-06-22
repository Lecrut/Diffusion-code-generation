import statistics

def compute_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    scores = [85, 92, 78, 90, 88, 76, 95, 89, 91, 84]
    result = compute_mean(scores)
    print(result)