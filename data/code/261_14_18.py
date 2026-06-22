import heapq

def calculate_median(data):
    min_heap = []
    max_heap = []

    def push(num):
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

    def balance():
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    def get_median():
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        else:
            return -max_heap[0]

    for num in data:
        push(num)
        balance()

    return get_median()

if __name__ == '__main__':
    list1 = [3, 5, 1, 4, 2]
    list2 = [6, 8, 7, 9, 10]
    list3 = []
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")