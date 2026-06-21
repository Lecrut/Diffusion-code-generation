class MergeSort:
    @staticmethod
    def merge(left, right):
        sorted_list = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])
        return sorted_list

    def sort(self, data):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left_half = self.sort(data[:mid])
        right_half = self.sort(data[mid:])

        return self.merge(left_half, right_half)

if __name__ == '__main__':
    sample_data = [34, 7, 23, 32, 5, 62]
    sorter = MergeSort()
    sorted_data = sorter.sort(sample_data)
    print(sorted_data)