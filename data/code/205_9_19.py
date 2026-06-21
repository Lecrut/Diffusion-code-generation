class MergeSort:
    def __init__(self):
        self._temp_array = []

    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

    @staticmethod
    def sort(data):
        sorter = MergeSort()
        return sorter.merge_sort(data)

if __name__ == '__main__':
    sample_data = [34, 7, 23, 32, 5, 62]
    sorted_data = MergeSort.sort(sample_data)
    print(sorted_data)