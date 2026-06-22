import heapq

def median(l):
    return l[len(l) // 2] if len(l) % 2 == 1 else (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

if __name__ == '__main__':
    sample = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(median(sample))