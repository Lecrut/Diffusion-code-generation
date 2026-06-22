def count_items(lst):
    return sum(1 for _ in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(count_items(sample_list))