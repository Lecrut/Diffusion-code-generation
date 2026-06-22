class VolumeManager:
    def __init__(self):
        self.volumes = []
        self.volume_map = {}

    def store(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        existing_index = None
        for i, entry in enumerate(self.volumes):
            if entry['key'] == key:
                existing_index = i
                break
        new_entry = {'key': key, 'value': value}
        if existing_index is not None:
            self.volumes[existing_index] = new_entry
        else:
            self.volumes.append(new_entry)
        self.volume_map[key] = value

    def add(self, key, delta):
        if key not in self.volume_map:
            raise KeyError(f"Key {key} does not exist")
        current_value = self.volume_map[key]
        new_value = current_value + delta
        self.store(key, new_value)
        return new_value

    def retrieve(self, key):
        if key not in self.volume_map:
            raise KeyError(f"Key {key} does not exist")
        return self.volume_map[key]

    def list_all(self):
        return dict(self.volume_map)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store("room_a", 100.0)
    manager.store("room_b", 200.5)
    manager.store("room_c", 300)
    print(manager.retrieve("room_a"))
    manager.add("room_a", 50.0)
    print(manager.retrieve("room_a"))
    manager.add("room_b", -20.5)
    print(manager.retrieve("room_b"))
    print(manager.list_all())