import statistics

def calculate_mean(scores):
    return statistics.mean(scores)

if __name__ == '__main__':
    test_scores = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [],
        'list3': [10.5, 20.5, 30.5],
        'list4': [-1, 5, 10, -5]
    }

    for key, scores in test_scores.items():
        print(f"Mean of {key}: {calculate_mean(scores)}")