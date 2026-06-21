if __name__ == '__main__':
    sample_data = ['red', 'blue', 'green', 'blue', 'red', 'red']
    freq_map = {item: sample_data.count(item) for item in set(sample_data)}
    print(freq_map)