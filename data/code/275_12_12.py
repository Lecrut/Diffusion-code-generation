class ListFlattener:
    @staticmethod
    def flatten_and_print(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                ListFlattener.flatten_and_print(item)
            else:
                print(item)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    ListFlattener.flatten_and_print(sample_data)