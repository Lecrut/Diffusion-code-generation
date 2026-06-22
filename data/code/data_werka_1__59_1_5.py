def find_middle_item(sequence):
    length = len(sequence)
    if length % 2 == 0:
        return sequence[length // 2 - 1:length // 2 + 1]
    else:
        return sequence[length // 2]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40, 50)
    print(find_middle_item(sample_list))
    print(find_middle_item(sample_tuple))