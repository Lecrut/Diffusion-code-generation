import heapq

def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    smaller = []
    larger = []
    
    for num in data:
        if len(smaller) == len(larger):
            heapq.heappush(larger, -heapq.heappushpop(smaller, -num))
        else:
            heapq.heappush(smaller, -heapq.heappushpop(larger, num))
    
    if len(smaller) == len(larger):
        return (-smaller[0] + larger[0]) / 2.0
    else:
        return -smaller[0]

if __name__ == '__main__':
    list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    list2 = [10.0, 5.0, 2.0, 7.0, 1.0]
    list3 = [5.5]
    list4 = []
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    try:
        print(f"Median of {list4}: {calculate_median(list4)}")
    except ValueError as e:
        print(e)