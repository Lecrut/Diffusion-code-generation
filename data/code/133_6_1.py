from collections import Counter
def check_truth_distribution(data):
    truth_counts = Counter(data)
    return dict(truth_counts)
if __name__ == '__main__':
    sample_data = ["True", "False", "True", "True", "False", "True", "False", "False"]
    distribution = check_truth_distribution(sample_data)
    print(distribution)