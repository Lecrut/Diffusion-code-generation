class IntegerSorter:
    @staticmethod
    def sort_integers(int_list):
        return sorted(int_list)

if __name__ == '__main__':
    sample_values = [13, 7, 22, 5, 8, 19]
    sorter = IntegerSorter()
    sorted_values = sorter.sort_integers(sample_values)
    print(sorted_values)