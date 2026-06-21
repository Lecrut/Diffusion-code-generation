class ItemCounter:
    @staticmethod
    def item_count_pairs(iterable):
        count = 0
        for item in iterable:
            yield item, count
            count += 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    pairs_generator = ItemCounter.item_count_pairs(sample_list)
    for pair in pairs_generator:
        print(f'Item: {pair[0]}, Count: {pair[1]}')