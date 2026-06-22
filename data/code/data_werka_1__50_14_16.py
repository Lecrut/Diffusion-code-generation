def compute_element_wise_difference(list1, list2):
    result = []
    index1, index2 = 0, 0
    
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            result.append(list1[index1])
            index1 += 1
        elif list1[index1] > list2[index2]:
            result.append(list2[index2])
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    while index1 < len(list1):
        result.append(list1[index1])
        index1 += 1
    
    while index2 < len(list2):
        result.append(list2[index2])
        index2 += 1
    
    return result

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7]
    sample_list2 = [2, 4, 6, 8]
    difference = compute_element_wise_difference(sample_list1, sample_list2)
    print(difference)