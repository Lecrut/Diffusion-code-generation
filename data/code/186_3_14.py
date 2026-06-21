if __name__ == '__main__':
    sample_data = [(4, 3), (2, 1), (5, 0), (3, 2)]
    sorted_data = sorted(sample_data, key=lambda x: x[1], reverse=True)
    print(sorted_data)