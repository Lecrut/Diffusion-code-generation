import heapq
def sort_by_sign(numbers):
    positives = []
    negatives = []
    for num in numbers:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)
    positives.sort()
    negatives.sort(reverse=True)                                                            
    negatives.sort() 
    return positives + negatives
if __name__ == '__main__':
    sample_data = [-4, 7, -10, 0, 3, -8, 2]
    result = sort_by_sign(sample_data)
    print(result)