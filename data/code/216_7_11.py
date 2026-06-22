import heapq

def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    
    if n % 2 == 1:
        return heapq.nsmallest(1, data)[-1]
    else:
        mid1 = heapq.nsmallest(n // 2, data)[-1]
        mid2 = heapq.nsmallest(n // 2 + 1, data)[-1]
        return (mid1 + mid2) / 2.0

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 4, 7, 2, 15]
    list4 = []
    list5 = [1, 2, 3, 4, 5, 6]

    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    try:
        print(f"Median of {list4}: {calculate_median(list4)}")
    except ValueError as e:
        print(e)
    print(f"Median of {list5}: {calculate_median(list5)}")