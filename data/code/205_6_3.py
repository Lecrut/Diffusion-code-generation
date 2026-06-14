import heapq
def sort_with_heapq(items):
    heapq.heapify(items)
    return sorted(items)
if __name__ == '__main__':
    data = [5, 2, 8, 1, 9]
    sorted_data = sort_with_heapq(data)
    print(sorted_data)