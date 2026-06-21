def compute_difference(list1, list2):
    diff = []
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)
    
    while i < len1 and j < len2:
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            diff.append(list1[i])
            i += 1
        else:
            diff.append(list2[j])
            j += 1
    
    while i < len1:
        diff.append(list1[i])
        i += 1
    
    while j < len2:
        diff.append(list2[j])
        j += 1
    
    return diff

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7]
    sample_list2 = [2, 3, 6, 8]
    result = compute_difference(sample_list1, sample_list2)
    print(result)