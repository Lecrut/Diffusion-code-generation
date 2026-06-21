if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = [sample_list[i] for i in range(len(sample_list)-1, -1, -1)]
    print(reversed_list)