class VolumeManager:
    def __init__(self):
        self.volumes = {}

    def store(self, name, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Volume must be a number")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        self.volumes[name] = float(value)

    def add(self, name, increment):
        if name not in self.volumes:
            raise KeyError(f"Volume '{name}' not found")
        if not isinstance(increment, (int, float)):
            raise ValueError("Increment must be a number")
        self.volumes[name] += increment
        if self.volumes[name] < 0:
            self.volumes[name] = 0

    def retrieve(self, name):
        if name not in self.volumes:
            return None
        return self.volumes[name]

    def get_all(self):
        return dict(self.volumes)

if __name__ == '__main__':
    vm = VolumeManager()
    vm.store("cylinder_a", 100.5)
    vm.store("sphere_b", 200.0)
    vm.add("cylinder_a", 50.5)
    print(vm.retrieve("cylinder_a"))
    print(vm.retrieve("sphere_b"))
    print(vm.get_all())
    print(vm.retrieve("non_existent"))