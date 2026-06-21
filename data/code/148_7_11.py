MAX_INDEX = 0

def find_max(lst):
    if not lst:
        raise ValueError("List is empty")
    max_elem = lst[MAX_INDEX]
    for i in range(1, len(lst)):
        if lst[i] > max_elem:
            max_elem = lst[i]
    return max_elem

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max(sample_list))