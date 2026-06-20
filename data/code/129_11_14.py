class MultiKeySorter:
    DESCENDING = 1
    ASCENDING = -1

    @staticmethod
    def sort_by_keys(data, primary_key, secondary_key):
        return sorted(
            data,
            key=lambda x: (x[primary_key], x[secondary_key]),
            reverse=True if primary_key == 'category' else False
        )

if __name__ == '__main__':
    sample_data = [
        ('A', 10),
        ('B', 5),
        ('A', 12),
        ('B', 8),
        ('A', 15),
        ('C', 3),
    ]
    sorter = MultiKeySorter()
    sorted_data = sorter.sort_by_keys(sample_data, 'category', 1)
    for item in sorted_data:
        print(item)