class GroupBySecond:
    def group(self, tuples_list):
        grouped_dict = {}
        for key, value in tuples_list:
            if value not in grouped_dict:
                grouped_dict[value] = []
            grouped_dict[value].append(key)
        return grouped_dict

if __name__ == '__main__':
    sorter = GroupBySecond()
    data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    category_groups = sorter.group(data)
    print(category_groups)