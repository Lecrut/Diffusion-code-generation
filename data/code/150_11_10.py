class ListFilter:
    @staticmethod
    def remove_value(lst, value):
        return [item for item in lst if item != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 3]
    value_to_remove = 3
    filtered_list = ListFilter.remove_value(sample_list, value_to_remove)
    print(filtered_list)