if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = [sample_list.pop() for _ in range(len(sample_list))]
    print(reversed_list)