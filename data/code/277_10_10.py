def count_items(lst):
    count = 0
    for item in lst:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = count_items(sample_list)
    print(result)