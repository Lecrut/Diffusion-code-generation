def merge_unique_colors(list1, list2):
    return list(set(list1 + list2))

if __name__ == '__main__':
    sample_list1 = ["red", "blue", "green"]
    sample_list2 = ["yellow", "green", "purple"]
    merged_colors = merge_unique_colors(sample_list1, sample_list2)
    print(merged_colors)