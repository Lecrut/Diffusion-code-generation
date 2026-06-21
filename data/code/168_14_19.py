def segment_tuples_by_sign(tuples):
    positive = [t for t in tuples if t[0] >= 0]
    negative = [t for t in tuples if t[0] < 0]
    return positive, negative

if __name__ == '__main__':
    sample_tuples = [(1, 'a'), (-2, 'b'), (3, 'c'), (-4, 'd')]
    result = segment_tuples_by_sign(sample_tuples)
    print(result)