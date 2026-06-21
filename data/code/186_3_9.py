if __name__ == '__main__':
    sample_tuples = [(4, 3), (2, 1), (5, 0), (3, 2)]
    sorted_tuples = sorted(sample_tuples, key=lambda x: x[1], reverse=True)
    print(sorted_tuples)