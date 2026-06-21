if __name__ == '__main__':
    sample_data = [(1, 2), (3, 1), (5, 0)]
    sorted_data = sorted(sample_data, key=lambda x: x[1], reverse=True)
    print(sorted_data)