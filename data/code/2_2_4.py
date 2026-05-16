class VolumeManager:
    def __init__(self):
        self._volumes = {}
    def store_volume(self, name, volume):
        if not isinstance(name, str) or not isinstance(volume, (int, float)):
            raise TypeError("Name must be a string and volume must be a number.")
        self._volumes[name] = volume
    def add_volume(self, name, volume):
        if not isinstance(name, str) or not isinstance(volume, (int, float)):
            raise TypeError("Name must be a string and volume must be a number.")
        if name in self._volumes:
            self._volumes[name] += volume
        else:
            self._volumes[name] = volume
    def retrieve_volume(self, name):
        return self._volumes.get(name)
    def get_all_volumes(self):
        return self._volumes.copy()
if __name__ == '__main__':
    manager = VolumeManager()
    manager.store_volume("RoomA", 150.5)
    manager.store_volume("Kitchen", 30.0)
    manager.store_volume("LivingRoom", 450.75)
    print("--- Initial Volumes ---")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    print(f"LivingRoom: {manager.retrieve_volume('LivingRoom')}")
    manager.add_volume("RoomA", 25.25)
    manager.add_volume("Kitchen", 5.5)
    print("\n--- Volumes After Addition ---")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    print("\n--- All Stored Volumes ---")
    print(manager.get_all_volumes())