class Data:
    pass
class StringData(Data):
    pass
class IntegerData(Data):
    pass
def filter_by_class(data_list, class_to_remove):
    result = []
    for item in data_list:
        if not isinstance(item, class_to_remove):
            result.append(item)
    return result
if __name__ == '__main__':
    mixed_list = [1, "hello", Data(), 2.5, StringData(), 3, None, IntegerData()]
    class_to_remove = Data
    filtered_list = filter_by_class(mixed_list, class_to_remove)
    print(filtered_list)