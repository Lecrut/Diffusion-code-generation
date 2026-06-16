import heapq
def sort_positive_before_negative(numbers):
    positive_heap = []
    negative_list = []
    for num in numbers:
        if num > 0:
            heapq.heappush(positive_heap, -num)                                                      
        else:
            negative_list.append(num)
    sorted_positives = [-x for x in positive_heap]
    return sorted_positives + negative_list
if __name__ == '__main__':
    sample_data = [3, -1, 4, -2, 5, -6, 7, -8, 9]
    result = sort_positive_before_negative(sample_data)
    print(result)