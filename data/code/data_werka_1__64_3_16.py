def find_last_index(lst, value):
    return len(lst) - 1 - lst[::-1].index(value) if value in lst else -1

if __name__ == '__main__':
    sample_list = [7, 8, 9, 5, 3, 5, 2]
    target_value = 5
    last_occurrence_index = find_last_index(sample_list, target_value)
    print(last_occurrence_index)