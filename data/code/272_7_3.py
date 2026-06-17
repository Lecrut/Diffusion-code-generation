import random
def alphabetical_sort(string_iterable):
    return sorted(list(string_iterable))
if __name__ == '__main__':
    sample1 = ["banana", "apple", "cherry", "date"]
    print(f"Input: {sample1}")
    result1 = alphabetical_sort(sample1)
    print(f"Output: {result1}")
    sample2 = ["zebra", "ant", "bear", "cat"]
    print(f"Input: {sample2}")
    result2 = alphabetical_sort(sample2)
    print(f"Output: {result2}")
    sample3 = ["hello", "world", "python", "java"]
    print(f"Input: {sample3}")
    result3 = alphabetical_sort(sample3)
    print(f"Output: {result3}")
    sample4 = ["a", "b", "c", "d", "e"]
    print(f"Input: {sample4}")
    result4 = alphabetical_sort(sample4)
    print(f"Output: {result4}")