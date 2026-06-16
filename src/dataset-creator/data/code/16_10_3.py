def count_elements(lst):
    return sum(1 for _ in lst)
if __name__ == '__main__':
    data = [10, 20, 30, 'a', None]
    total_count = count_elements(data)
    print(total_count)