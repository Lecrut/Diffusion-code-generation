INITIAL_COUNT = 0

def count_items(lst):
    count = INITIAL_COUNT
    for item in lst:
        count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(count_items(sample_list))