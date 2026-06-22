def count_items(lst):
    count = 0
    for item in lst:
        count += 1
    return count

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    result = count_items(sample_list)
    print(result)