import random

class RandomValueFetcher:
    def __init__(self, data):
        self.data = data

    def fetch_random(self):
        if not self.data:
            return None
        keys = list(self.data.keys())
        target = random.choice(keys)
        return self.data[target]

if __name__ == '__main__':
    inventory = {'hammer': 10, 'screwdriver': 15, 'wrench': 5, 'pliers': 8}
    empty_inventory = {}
    fetcher1 = RandomValueFetcher(inventory)
    fetcher2 = RandomValueFetcher(empty_inventory)
    print(fetcher1.fetch_random())
    print(fetcher2.fetch_random())