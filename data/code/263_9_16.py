def find_unique_elements(set1, set2):
    return (set1 - set2) | (set2 - set1)

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {30, 40, 50, 60}
    unique_elements = find_unique_elements(sample_set1, sample_set2)
    print(unique_elements)