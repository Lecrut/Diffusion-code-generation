if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 1), (5, 0)]
    if not all(isinstance(t, tuple) and len(t) == 2 for t in sample_tuples):
        raise ValueError("Sample must be a list of tuples with two elements each.")
    
    sorted_tuples = sorted(sample_tuples, key=lambda x: x[1], reverse=True)
    print(sorted_tuples)