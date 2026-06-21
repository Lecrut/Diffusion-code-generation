class ListFlattener:
    @staticmethod
    def flatten(nested_list):
        flat_list = []
        ListFlattener._flatten_helper(nested_list, flat_list)
        return flat_list

    @staticmethod
    def _flatten_helper(item, flat_list):
        if isinstance(item, list):
            for sub_item in item:
                ListFlattener._flatten_helper(sub_item, flat_list)
        else:
            flat_list.append(item)

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(ListFlattener.flatten(sample_list))