if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50, 40]
    TARGET_VALUE = 40
    last_index = len(SAMPLE_LIST) - SAMPLE_LIST[::-1].index(TARGET_VALUE) - 1 if TARGET_VALUE in SAMPLE_LIST else -1
    print(last_index)