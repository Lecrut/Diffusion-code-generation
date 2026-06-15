class Sorter:
    def sort_list(self, data):
        data.sort()
if __name__ == '__main__':
    sorter = Sorter()
    sample_list = [5, 2, 8, 1, 9, 4]
    print("Original list:", sample_list)
    sorter.sort_list(sample_list)
    print("Sorted list:", sample_list)