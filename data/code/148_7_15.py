MAX_VALUE = float('-inf')

def find_max(lst):
    max_elem = MAX_VALUE
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max(sample_list))