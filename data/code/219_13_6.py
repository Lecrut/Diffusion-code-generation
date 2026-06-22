def find_largest_value(dictionary):
    if not dictionary:
        return None
    largest = max(dictionary.values())
    return largest

if __name__ == '__main__':
    sample_dict = {'apple': 150, 'banana': 300, 'cherry': 200}
    print(find_largest_value(sample_dict))