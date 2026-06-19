if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 4, 5]
    TARGET_VALUE = 4
    last_index = max([i for i, x in enumerate(SAMPLE_LIST) if x == TARGET_VALUE], default=-1)
    print(last_index)