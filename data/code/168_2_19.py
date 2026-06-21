class TupleGrouper:
    def group_by_second_element(self, tuples_list):
        grouped_dict = {}
        for item in tuples_list:
            if len(item) != 2:
                raise ValueError("Each tuple must contain exactly two elements")
            key, value = item
            if value not in grouped_dict:
                grouped_dict[value] = []
            grouped_dict[value].append(key)
        return grouped_dict

if __name__ == '__main__':
    grouper = TupleGrouper()
    sample_data = [(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (5, 'b')]
    result = grouper.group_by_second_element(sample_data)
    print(result)