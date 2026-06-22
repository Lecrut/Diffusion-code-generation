def are_elements_unique(lst):
    seen = {}
    for item in lst:
        if item in seen:
            return False
        seen[item] = True
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))