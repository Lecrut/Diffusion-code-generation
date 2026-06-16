import heapq
def sort_by_sign(numbers):
    positives = [x for x in numbers if x > 0]
    zeros = [x for x in numbers if x == 0]
    negatives = [-(-x) for x in numbers if x < 0]
    positives.sort()
    zeros.sort()
    return positives + zeros + negatives
if __name__ == '__main__':
    sample_data = [3, -1, 42, -5, 0, 7, -8, 9]
    sorted_result = sort_by_sign(sample_data)
    print(sorted_result)