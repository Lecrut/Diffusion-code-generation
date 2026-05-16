def sort_tuples_by_value(data):
    return sorted(data, key=lambda item: item[1], reverse=True)
if __name__ == '__main__':
    data = [('apple', 5), ('banana', 12), ('cherry', 3)]
    sorted_data = sort_tuples_by_value(data)
    print(sorted_data)