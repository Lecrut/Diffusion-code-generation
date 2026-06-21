def compute_elementwise_difference(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("Both lists must contain only integers.")
    
    diff = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            diff.append(list1[i])
            i += 1
        else:
            diff.append(list2[j])
            j += 1
    
    while i < len(list1):
        diff.append(list1[i])
        i += 1
    
    while j < len(list2):
        diff.append(list2[j])
        j += 1
    
    return diff

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7]
    sample_list2 = [2, 3, 6, 8]
    
    try:
        result = compute_elementwise_difference(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)