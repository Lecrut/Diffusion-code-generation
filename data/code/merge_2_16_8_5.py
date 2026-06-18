def count_elements(data):
    return len([x for x in data]) if isinstance(data, list) else 0
if __name__ == '__main__':
    sample_list = [1, "apple", None, [], {"key": "val"}, True]
    print(count_elements(sample_list))