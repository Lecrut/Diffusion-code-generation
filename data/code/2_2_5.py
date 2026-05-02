class VolumeManager:
    def __init__(self):
        self.volumes = {}
    def store_volume(self, name, volume):
        if not isinstance(name, str) or not isinstance(volume, (int, float)):
            raise TypeError("Name must be a string and volume must be a number.")
        self.volumes[name] = volume
    def add_volume(self, name, volume):
        if not isinstance(name, str) or not isinstance(volume, (int, float)):
            raise TypeError("Name must be a string and volume must be a number.")
        if name in self.volumes:
            self.volumes[name] += volume
        else:
            self.volumes[name] = volume
    def retrieve_volume(self, name):
        return self.volumes.get(name)
if __name__ == '__main__':
    manager = VolumeManager()
    manager.store_volume("RoomA", 15.5)
    manager.store_volume("Kitchen", 10.0)
    manager.store_volume("LivingRoom", 25.75)
    print("Initial Volumes:")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    print(f"LivingRoom: {manager.retrieve_volume('LivingRoom')}")
    manager.add_volume("RoomA", 5.0)
    manager.add_volume("Kitchen", 2.5)
    print("\nVolumes after adding:")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    print(f"LivingRoom: {manager.retrieve_volume('LivingRoom')}")