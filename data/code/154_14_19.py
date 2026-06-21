def tally_items(sequence):
    counter = {}
    for item in sequence:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return dict(sorted(counter.items()))

class ItemTally:
    def __init__(self, sequence):
        self.counter = tally_items(sequence)

    def get_tally(self):
        return self.counter

if __name__ == '__main__':
    sample_list = [3, 1, 2, 3, 4, 5, 1, 2, 1]
    item_tally = ItemTally(sample_list)
    print("Item tally:", item_tally.get_tally())