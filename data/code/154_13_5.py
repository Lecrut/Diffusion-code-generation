if __name__ == '__main__':
    sample_list = ['red', 'blue', 'green', 'red', 'blue', 'red']
    frequency_map = {item: sample_list.count(item) for item in set(sample_list)}
    print(frequency_map)