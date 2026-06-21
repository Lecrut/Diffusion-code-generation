def remove_duplicates(data_list, item_to_remove):
    new_list = []
    for item in data_list:
        if item != item_to_remove:
            new_list.append(item)
    return new_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    value_to_remove = 3
    result = remove_duplicates(sample_list, value_to_remove)
    print(result)
    another_sample = ['apple', 'banana', 'cherry', 'apple']
    fruit_to_remove = 'apple'
    new_list = remove_duplicates(another_sample, fruit_to_remove)
    print(new_list)