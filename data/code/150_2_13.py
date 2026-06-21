class ListModifier:
    @staticmethod
    def remove_all_instances(lst, item):
        while item in lst:
            lst.remove(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5, 2]
    ListModifier.remove_all_instances(sample_list, 2)
    print(sample_list)