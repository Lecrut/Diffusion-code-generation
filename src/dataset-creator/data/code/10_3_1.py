import heapq
def sort_by_sign(numbers):
    pos = [x for x in numbers if x >= 0]
    neg = [x for x in numbers if x < 0]
    return pos + neg
if __name__ == '__main__':
    sample_data = [-5, -12, 3, 7, -8, 0, 4, -9]
    sorted_result = sort_by_sign(sample_data)
    print(sorted_result)