if __name__ == '__main__':
    tuples = [(4, 3), (1, 2), (5, 0), (2, 1)]
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
    print(sorted_tuples)