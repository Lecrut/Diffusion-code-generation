class AscendingSorter:
    @staticmethod
    def sort(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    sorter = AscendingSorter()
    sorted_data = sorter.sort(sample_values)
    print(*sorted_data)