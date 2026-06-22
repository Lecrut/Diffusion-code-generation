def compute_average(scores_tuple):
    return sum([score for score in scores_tuple]) / len(scores_tuple)

if __name__ == '__main__':
    scores = (85, 92, 78, 90, 88)
    print(compute_average(scores))