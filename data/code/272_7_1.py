import random
def alphabetical_sort(iterable):
    return sorted(list(iterable))
if __name__ == '__main__':
    sample1 = ["banana", "apple", "cherry", "date"]
    result1 = alphabetical_sort(sample1)
    print(f"Sample 1 Input: {sample1}")
    print(f"Sample 1 Output: {result1}")
    sample2 = ["zebra", "ant", "bear", "cat"]
    result2 = alphabetical_sort(sample2)
    print(f"Sample 2 Input: {sample2}")
    print(f"Sample 2 Output: {result2}")
    sample3 = ["hello", "world", "python", "java"]
    result3 = alphabetical_sort(sample3)
    print(f"Sample 3 Input: {sample3}")
    print(f"Sample 3 Output: {result3}")
    sample4 = ["a", "b", "c", "d", "e"]
    result4 = alphabetical_sort(sample4)
    print(f"Sample 4 Input: {sample4}")
    print(f"Sample 4 Output: {result4}")