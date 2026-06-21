class StoreBatchGenerator:

    def __init__(self):
        self.stores = ['StoreA', 'StoreB', 'StoreC', 'StoreD', 'StoreE', 'StoreF', 'StoreG', 'StoreH', 'StoreI', 'StoreJ']
        self.index = 0

    def get_batch(self):
        while self.index < len(self.stores):
            batch = []
            for _ in range(50):
                if self.index >= len(self.stores):
                    break
                batch.append(self.stores[self.index])
                self.index += 1
            yield batch
if __name__ == '__main__':
    generator = StoreBatchGenerator()
    for i, batch in enumerate(generator.get_batch()):
        print(f'Batch {i + 1}: {batch}')