class VolumeManager:
    def __init__(self):
        self._volumes = {}

    def add_volume(self, name, value, unit="cubic_meters"):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be numeric")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        self._volumes[name] = {"value": float(value), "unit": unit}

    def get_volume(self, name):
        if name not in self._volumes:
            return None
        return self._volumes[name]

    def store_volume(self, name, value, unit="cubic_meters"):
        self.add_volume(name, value, unit)

    def list_volumes(self):
        return dict(self._volumes)

    def remove_volume(self, name):
        if name in self._volumes:
            del self._volumes[name]
            return True
        return False

    def update_volume(self, name, new_value=None, new_unit=None):
        if name not in self._volumes:
            return False
        if new_value is not None:
            if not isinstance(new_value, (int, float)):
                raise TypeError("Volume value must be numeric")
            if new_value < 0:
                raise ValueError("Volume cannot be negative")
            self._volumes[name]["value"] = float(new_value)
        if new_unit is not None:
            if not isinstance(new_unit, str) or not new_unit:
                raise ValueError("Unit must be a non-empty string")
            self._volumes[name]["unit"] = new_unit
        return True

if __name__ == '__main__':
    vm = VolumeManager()
    vm.add_volume("tank_a", 100.5, "liters")
    vm.add_volume("tank_b", 250, "gallons")
    vm.store_volume("tank_c", 50.0, "cubic_meters")
    print(vm.get_volume("tank_a"))
    print(vm.get_volume("tank_b"))
    print(vm.get_volume("tank_c"))
    vm.update_volume("tank_a", 110.0)
    print(vm.get_volume("tank_a"))
    print(vm.list_volumes())
    vm.remove_volume("tank_b")
    print(vm.get_volume("tank_b"))
    print(vm.list_volumes())