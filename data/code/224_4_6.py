EMPTY_SEQUENCE_ERROR = 'Input sequence is empty'

def calculate_mean(scores):
    if not scores:
        raise ValueError(EMPTY_SEQUENCE_ERROR)
    return sum(scores) / len(scores)
if __name__ == '__main__':
    sample_scores = (85, 90, 78, 92)
    print(calculate_mean(sample_scores))