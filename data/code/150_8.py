class Data:
    pass
class Number:
    pass
def filter_by_class(data_list, class_to_remove):
    result = []
    for item in data_list:
        if not isinstance(item, class_to_remove):
            result.append(item)
    return result
if __name__ == '__main__':
    mixed_list = [1, "hello", Data(), 3.14, Number(), "world", 5]
    class_to_remove_type = Data
    filtered_list = filter_by_class(mixed_list, class_to_remove_type)
    print(filtered_list)