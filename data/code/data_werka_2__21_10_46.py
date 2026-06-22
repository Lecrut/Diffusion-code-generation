class IntegerSorter:
    @staticmethod
    def sort_integers(int_list):
        return sorted(int_list)

if __name__ == '__main__':
    sample_values = [13, 27, 8, 45, 9, 10]
    sorted_values = IntegerSorter.sort_integers(sample_values)
    print(sorted_values)