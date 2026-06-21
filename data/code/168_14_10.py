def segment_tuples_by_sign(tuples):
    return [[t for t in tuples if t[0] > 0], [t for t in tuples if t[0] < 0]]

if __name__ == '__main__':
    sample_values = [(1, 'a'), (-2, 'b'), (3, 'c'), (-4, 'd')]
    print(segment_tuples_by_sign(sample_values))