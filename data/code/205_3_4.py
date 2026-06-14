class ItemSorter:
    def sort_items(self, data):
        return sorted(data)
if __name__ == '__main__':
    sorter = ItemSorter()
    sample_data = [3.14, 1.0, 5, 2.718, -1.5]
    sorted_data = sorter.sort_items(sample_data)
    print(sorted_data)