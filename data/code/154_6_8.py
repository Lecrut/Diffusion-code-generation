if __name__ == '__main__':
    SAMPLE_LIST = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    result = [(item, SAMPLE_LIST.count(item)) for item in set(SAMPLE_LIST)]
    print(result)