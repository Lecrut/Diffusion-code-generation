class Sorter:
    @staticmethod
    def sort_tuple(items):
        return tuple(sorted(items))

if __name__ == '__main__':
    sample_data = (3.14, 1, 5.5, 2, 8.9)
    sorted_data = Sorter.sort_tuple(sample_data)
    print("Sorted tuple:", sorted_data)