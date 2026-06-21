class StoreGenerator:

    def __init__(self):
        self.stores = ['Store1', 'Store2', 'Store3', 'Store4', 'Store5', 'Store6', 'Store7', 'Store8', 'Store9', 'Store10']

    def batch_generator(self, batch_size=50):
        for i in range(0, len(self.stores), batch_size):
            yield self.stores[i:i + batch_size]
if __name__ == '__main__':
    generator = StoreGenerator()
    for batch in generator.batch_generator():
        print(batch)