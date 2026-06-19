def find_middle_item(sequence):
    return sequence[len(sequence) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(find_middle_item(sample_list))