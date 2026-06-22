def calculate_average(scores_tuple):
    return sum([score for score in scores_tuple]) / len(scores_tuple)

if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92, 88)
    print(calculate_average(sample_scores))