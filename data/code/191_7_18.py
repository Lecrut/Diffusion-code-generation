class ListMerger:
    @staticmethod
    def merge(list_x, list_y):
        return list_x + list_y

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    merged_list = ListMerger.merge(list_a, list_b)
    print(merged_list)