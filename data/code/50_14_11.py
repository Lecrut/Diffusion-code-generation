def element_wise_difference(list1, list2):
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("Both lists must contain only integers.")
    
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            i += 1
            j += 1
    
    while i < len(list1):
        result.append(list1[i])
        i += 1
    
    while j < len(list2):
        result.append(list2[j])
        j += 1
    
    return result

if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    difference = element_wise_difference(list1, list2)
    print(difference)