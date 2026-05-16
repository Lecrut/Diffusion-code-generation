def find_final_index(indices):
    if not indices:
        return -1
    return max(indices)
if __name__ == '__main__':
    sample1 = [1, 5, 3, 8, 2]
    print(find_final_index(sample1))
    sample2 = [10, 20, 5]
    print(find_final_index(sample2))
    sample3 = [42]
    print(find_final_index(sample3))
    sample4 = []
    print(find_final_index(sample4))