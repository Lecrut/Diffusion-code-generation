def find_last_occurrence_index(data, item):
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == item:
            last_index = i
            break
    return last_index

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 5, 2, 8, 5, 3]
    TARGET_ITEM_1 = 5
    result_1 = find_last_occurrence_index(SAMPLE_LIST_1, TARGET_ITEM_1)
    print(f"List: {SAMPLE_LIST_1}, Item: {TARGET_ITEM_1}, Last Index: {result_1}")

    SAMPLE_LIST_2 = ['a', 'b', 'c', 'a', 'd', 'a']
    TARGET_ITEM_2 = 'a'
    result_2 = find_last_occurrence_index(SAMPLE_LIST_2, TARGET_ITEM_2)
    print(f"List: {SAMPLE_LIST_2}, Item: {TARGET_ITEM_2}, Last Index: {result_2}")

    SAMPLE_LIST_3 = [10, 20, 30]
    TARGET_ITEM_3 = 5
    result_3 = find_last_occurrence_index(SAMPLE_LIST_3, TARGET_ITEM_3)
    print(f"List: {SAMPLE_LIST_3}, Item: {TARGET_ITEM_3}, Last Index: {result_3}")