class MedianFinder:
    @staticmethod
    def find_median(sorted_list):
        n = len(sorted_list)
        if n % 2 == 1:
            return sorted_list[n // 2]
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            return (sorted_list[middle_left_index] + sorted_list[middle_right_index]) / 2.0

if __name__ == '__main__':
    sample_lists = [
        [1, 3, 8, 9, 15],
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [1, 2, 3, 4],
        [5, 15]
    ]
    
    for lst in sample_lists:
        print(f"List: {lst}, Median Value: {MedianFinder.find_median(lst)}")