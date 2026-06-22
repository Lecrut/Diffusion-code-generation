class VolumeDataStore:
    def __init__(self):
        self.bases = []
        self.scalars = []

    def store(self, base_volume):
        self.bases.append(base_volume)
        self.scalars.append(1.0)

    def scale(self, factor):
        for i in range(len(self.scalars)):
            self.scalars[i] *= factor

    def get(self, index):
        return self.bases[index] * self.scalars[index]

    def get_all(self):
        return [self.bases[i] * self.scalars[i] for i in range(len(self.bases))]

if __name__ == '__main__':
    store = VolumeDataStore()
    store.store(10.0)
    store.store(20.0)
    store.store(30.0)
    store.scale(2.0)
    print(store.get(0))
    print(store.get(1))
    print(store.get(2))
    print(store.get_all())
    store.store(40.0)
    print(store.get(3))
    store.scale(0.5)
    print(store.get_all())