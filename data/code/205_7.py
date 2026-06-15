def custom_sort(string_list):
    return sorted(string_list, key=len)
if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "orange", "grape"]
    sorted_data = custom_sort(data)
    print(sorted_data)