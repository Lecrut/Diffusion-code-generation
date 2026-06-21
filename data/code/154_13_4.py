if __name__ == '__main__':
    SAMPLE_LIST = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    FREQUENCY_MAP = {item: SAMPLE_LIST.count(item) for item in set(SAMPLE_LIST)}
    print(FREQUENCY_MAP)