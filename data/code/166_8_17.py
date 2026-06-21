def merge_unique_colors(list1, list2):
    return list(set(list1 + list2))

if __name__ == '__main__':
    colors1 = ['red', 'blue', 'green']
    colors2 = ['blue', 'yellow', 'black']
    print(merge_unique_colors(colors1, colors2))