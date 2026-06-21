class Sorter:
    @staticmethod
    def sort_ascending(numbers):
        return sorted(numbers)

if __name__ == '__main__':
    sample_values = [12, 45, 7, 3, 89, 2]
    sorted_data = Sorter.sort_ascending(sample_values)
    print(*sorted_data)