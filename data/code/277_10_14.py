def count_items(lst):
    count = 0
    for item in lst:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    print(count_items(sample_list))