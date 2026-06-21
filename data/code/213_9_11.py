class ListFlattener:
    @staticmethod
    def flatten(nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(ListFlattener.flatten(item))
            else:
                result.append(item)
        return result

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    flattened_list = ListFlattener.flatten(sample_list)
    print(flattened_list)