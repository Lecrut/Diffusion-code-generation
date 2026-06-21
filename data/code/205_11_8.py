def sort_items(data):
    return sorted(data, key=lambda x: x.lower())

if __name__ == '__main__':
    unsorted_list = ['banana', 'Apple', 'cherry', 'date']
    sorted_list = sort_items(unsorted_list)
    print(sorted_list)