import heapq
def sort_by_sign(numbers):
    pos = [x for x in numbers if x > 0]
    neg = sorted([x for x in numbers if x <= 0])
    return pos + neg
if __name__ == '__main__':
    sample_data = [-5, -2, 3, 1, -8, 4, 7, 0, -9]
    result = sort_by_sign(sample_data)
    print(result)