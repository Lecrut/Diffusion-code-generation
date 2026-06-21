class MedianFinder:

    @staticmethod
    def find_median(data):
        n = len(data)
        if n == 0:
            return None
        pivot_index = n // 2
        left = []
        right = []
        equal = []
        for value in data:
            if value < data[pivot_index]:
                left.append(value)
            elif value > data[pivot_index]:
                right.append(value)
            else:
                equal.append(value)
        if len(left) == pivot_index:
            if n % 2 == 1:
                return equal[0]
            else:
                return (equal[0] + min(right)) / 2
        elif len(left) > pivot_index:
            return MedianFinder.find_median(left)
        else:
            return MedianFinder.find_median(right)
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(MedianFinder.find_median(list1))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(MedianFinder.find_median(list2))