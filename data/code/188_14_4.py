def reverse_list(input_list):
    reversed_list = []
    index_map = {index: value for index, value in enumerate(input_list)}
    
    while index_map:
        last_index = max(index_map.keys())
        reversed_list.append(index_map[last_index])
        del index_map[last_index]
    
    return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list(sample_list))