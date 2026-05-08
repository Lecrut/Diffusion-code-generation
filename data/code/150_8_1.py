class MixedDataRemover:
    def remove_class(self, data_list, class_type):
        result = []
        for item in data_list:
            if not isinstance(item, class_type):
                result.append(item)
        return result
if __name__ == '__main__':
    data = [1, "hello", 3.14, True, [1, 2], "world", 42]
    class_to_remove = int
    remover = MixedDataRemover()
    result = remover.remove_class(data, class_to_remove)
    print(result)