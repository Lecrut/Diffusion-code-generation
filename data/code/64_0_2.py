import sys
def find_last_occurrence_index(data, item):
    last_index = -1
    for i in range(len(data)):
        if data[i] == item:
            last_index = i
    return last_index
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 3, 5, 9]
    target_item = 5
    result = find_last_occurrence_index(sample_list, target_item)
    print(result)