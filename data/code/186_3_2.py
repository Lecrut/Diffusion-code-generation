if __name__ == '__main__':
    sample_list = [(1, 2), (3, 1), (5, 0)]
    sorted_list = sorted(sample_list, key=lambda x: x[1], reverse=True)
    print(sorted_list)