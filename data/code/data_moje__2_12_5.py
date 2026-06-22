import math

class VolumeStorage:
    def __init__(self, base_volume=1.0):
        self.base_volume = base_volume
        self.scale_factors = {}

    def set_volume(self, volume):
        if volume <= 0:
            raise ValueError("Volume must be positive")
        self.base_volume = volume

    def add_measurement(self, key, multiplier):
        if multiplier <= 0:
            raise ValueError("Multiplier must be positive")
        self.scale_factors[key] = multiplier

    def get_measurement(self, key):
        if key not in self.scale_factors:
            raise KeyError(f"Measurement key '{key}' not found")
        multiplier = self.scale_factors[key]
        return self.base_volume * multiplier

    def get_all(self):
        return {k: self.base_volume * v for k, v in self.scale_factors.items()}

    def remove_measurement(self, key):
        if key not in self.scale_factors:
            raise KeyError(f"Measurement key '{key}' not found")
        del self.scale_factors[key]

    def update_base(self, new_base):
        if new_base <= 0:
            raise ValueError("Base volume must be positive")
        self.base_volume = new_base

if __name__ == '__main__':
    vs = VolumeStorage(10.0)
    vs.add_measurement("liters", 1.0)
    vs.add_measurement("gallons", 0.264172)
    vs.add_measurement("cubic_feet", 0.0353147)
    
    result_liters = vs.get_measurement("liters")
    result_gallons = vs.get_measurement("gallons")
    
    print(f"Liters: {result_liters}")
    print(f"Gallons: {result_gallons}")
    
    vs.update_base(100.0)
    new_gallons = vs.get_measurement("gallons")
    print(f"Gallons after base update: {new_gallons}")
    
    all_measurements = vs.get_all()
    print(f"All measurements: {all_measurements}")