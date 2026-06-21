def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

class ListFlattener:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def flatten(self):
        return flatten_list(self.nested_list)

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    flattener = ListFlattener(sample_list)
    print(flattener.flatten())