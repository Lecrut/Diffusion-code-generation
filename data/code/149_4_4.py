if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = [sample_list[idx] for idx in range(len(sample_list) - 1, -1, -1)]
    print(reversed_list)