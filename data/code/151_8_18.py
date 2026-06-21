class ListMerger:
    @staticmethod
    def merge_and_sort(list_a, list_b):
        combined_set = set(list_a + list_b)
        return sorted(combined_set)

if __name__ == '__main__':
    list_a_sample = [1.5, 2.3, 3.7]
    list_b_sample = [2.3, 4.1, 5.9]
    result = ListMerger.merge_and_sort(list_a_sample, list_b_sample)
    print(result)