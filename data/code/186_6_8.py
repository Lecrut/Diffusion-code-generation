class SortedGenerator:
    @staticmethod
    def sorted_items(items):
        items.sort()
        for item in items:
            yield item

if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_gen = SortedGenerator.sorted_items(sample_data)
    print(*sorted_gen)