def find_first_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 2]
    print(find_first_duplicate(sample_list))