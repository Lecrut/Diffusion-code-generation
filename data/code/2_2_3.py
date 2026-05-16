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
    manager.store_volume("RoomA", 150.5)
    manager.store_volume("Kitchen", 30.0)
    manager.store_volume("LivingRoom", 450.75)
    print("Initial Volumes:")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    print(f"LivingRoom: {manager.retrieve_volume('LivingRoom')}")
    manager.add_volume("RoomA", 25.25)
    print("\nVolumes after adding to RoomA:")
    print(f"RoomA: {manager.retrieve_volume('RoomA')}")
    manager.add_volume("Kitchen", 10.5)
    print("\nVolumes after adding to Kitchen:")
    print(f"Kitchen: {manager.retrieve_volume('Kitchen')}")
    manager.add_volume("Bedroom", 200)
    print("\nVolumes after adding Bedroom:")
    print(f"Bedroom: {manager.retrieve_volume('Bedroom')}")
    print("\nFinal Volume Dictionary:")
    print(manager.volumes)