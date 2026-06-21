class StoreNameGenerator:
    BATCH_SIZE = 50

    @staticmethod
    def get_store_names():
        store_names = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store F', 'Store G', 'Store H', 'Store I', 'Store J']
        return store_names

    def generate_batches(self):
        store_names = self.get_store_names()
        for i in range(0, len(store_names), self.BATCH_SIZE):
            yield store_names[i:i + self.BATCH_SIZE]
if __name__ == '__main__':
    generator = StoreNameGenerator()
    batches = list(generator.generate_batches())
    print(f'Total batches: {len(batches)}')
    for batch in batches:
        print(batch)