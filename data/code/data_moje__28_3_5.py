class FloatSorter:
    @staticmethod
    def sort_pair(a: float, b: float) -> tuple[float, float]:
        return min(a, b), max(a, b)

if __name__ == '__main__':
    sample_x = 55.5
    sample_y = 12.3
    sorted_values = FloatSorter.sort_pair(sample_x, sample_y)
    print(sorted_values)