class ItemSorter:
    def sort_items(self, data):
        return sorted(data)
if __name__ == '__main__':
    sorter = ItemSorter()
    sample_data = [3.14, 1.618, 2.718, 0.577]
    sorted_result = sorter.sort_items(sample_data)
    print(sorted_result)