if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequency_map = {item: sample_list.count(item) for item in set(sample_list)}
    print(frequency_map)