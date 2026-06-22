UNIQUE_CHECK_SET = set()

def are_elements_unique(lst):
    seen = UNIQUE_CHECK_SET.copy()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))
    print(are_elements_unique([1, 2, 3, 3, 5]))