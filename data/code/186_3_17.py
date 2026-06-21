if __name__ == '__main__':
    sample_data = [(4, 3), (1, 2), (7, 5), (3, 4)]
    sorted_data = sorted(sample_data, key=lambda x: x[1], reverse=True)
    print(sorted_data)