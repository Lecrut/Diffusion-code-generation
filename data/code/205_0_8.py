class AscendingSorter:
    @staticmethod
    def sort(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sample_values = [15, 23, 4, 89, 6]
    sorted_data = AscendingSorter.sort(sample_values)
    print(*sorted_data)