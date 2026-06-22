import array

class ScalableVolumeStore:
    def __init__(self, volumes):
        if not volumes:
            self.factor = 1.0
            self.raw_data = array.array('d', [])
        else:
            self.factor = 1.0
            self.raw_data = array.array('d', volumes)

    def scale_all(self, factor):
        self.factor *= factor

    def get_volume(self, index):
        return self.raw_data[index] * self.factor

    def get_volumes_batch(self, indices):
        result = []
        for i in indices:
            result.append(self.raw_data[i] * self.factor)
        return result

    def store_value(self, value, index=None):
        if index is None:
            self.raw_data.append(value)
        else:
            if index < len(self.raw_data):
                self.raw_data[index] = value
            else:
                while len(self.raw_data) < index:
                    self.raw_data.append(0.0)
                self.raw_data.append(value)

    def clear_scale(self):
        self.factor = 1.0

if __name__ == '__main__':
    initial_values = [10.5, 20.0, 15.25, 30.0]
    store = ScalableVolumeStore(initial_values)
    print(store.get_volume(0))
    print(store.get_volume(2))
    store.scale_all(2.0)
    print(store.get_volume(0))
    print(store.get_volume(2))
    store.store_value(50.0, 4)
    print(store.get_volume(4))
    store.clear_scale()
    print(store.get_volume(0))
    print(store.get_volumes_batch([0, 1, 2]))