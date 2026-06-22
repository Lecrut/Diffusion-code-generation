import statistics

def compute_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88]
    result = compute_mean(scores)
    print(result)