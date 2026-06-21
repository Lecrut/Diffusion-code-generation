if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    freq_map_instance = {item: sample_list.count(item) for item in set(sample_list)}
    print(freq_map_instance)
    print(freq_map_instance['apple'])
    print(freq_map_instance['banana'])
    print(freq_map_instance['orange'])