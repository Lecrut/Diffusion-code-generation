COUNT_MAP = {}

def count_list_items(iterable):
    global COUNT_MAP
    for item in iterable:
        if item in COUNT_MAP:
            COUNT_MAP[item] += 1
        else:
            COUNT_MAP[item] = 1

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    empty_list = []
    sample_list = [1, 2, 2, 3, 3, 3]

    count_list_items(list1)
    count_list_items(tuple2)
    count_list_items(empty_list)
    count_list_items(sample_list)

    print(f"Frequency of items in list1: {COUNT_MAP}")
    print(f"Frequency of items in tuple2: {COUNT_MAP}")
    print(f"Frequency of items in empty_list: {COUNT_MAP}")
    print(f"Frequency of items in sample_list: {COUNT_MAP}")