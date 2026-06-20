class MergeSort:
    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def sort(array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = MergeSort.sort(array[:mid])
            right_half = MergeSort.sort(array[mid:])

            return MergeSort.merge(left_half, right_half)
        else:
            return array

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    sorted_list = MergeSort.sort(sample_list)
    print(sorted_list)