class VolumeManager:
    def __init__(self):
        self._volumes = []
        self._index_map = {}

    def store(self, volume_id, measurement):
        if volume_id in self._index_map:
            old_index = self._index_map[volume_id]
            self._volumes[old_index] = (volume_id, measurement)
        else:
            self._index_map[volume_id] = len(self._volumes)
            self._volumes.append((volume_id, measurement))

    def add(self, volume_id, measurement):
        self.store(volume_id, measurement)

    def retrieve(self, volume_id):
        if volume_id in self._index_map:
            return self._volumes[self._index_map[volume_id]][1]
        return None

if __name__ == '__main__':
    manager = VolumeManager()
    manager.add('tank_1', 150.5)
    manager.add('tank_2', 200.0)
    manager.add('tank_1', 155.2)
    result = manager.retrieve('tank_1')
    print(result)
    result_two = manager.retrieve('tank_2')
    print(result_two)
    result_three = manager.retrieve('tank_3')
    print(result_three)