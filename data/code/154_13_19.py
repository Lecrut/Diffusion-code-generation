if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    frequency_map = {item: sample_data.count(item) for item in set(sample_data)}
    print(frequency_map)