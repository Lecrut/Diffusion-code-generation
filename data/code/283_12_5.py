FIRST_REPEATED = 'First Repeated Element'

def find_first_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    result = find_first_duplicate(sample_list)
    print(result if result is not None else FIRST_REPEATED)