from collections import Counter

def count_list_items(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list")
    return dict(Counter(data_list))

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(count_list_items(sample_list))