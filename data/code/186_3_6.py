if __name__ == '__main__':
    tuples = [(2, 3), (1, 4), (5, 2)]
    sorted_tuples = sorted(tuples, key=lambda x: x[1], reverse=True)
    print(sorted_tuples)