import math

class SparseVolume:

    def __init__(self):
        self.data = {}
        self.scale_factor = 1.0

    def set(self, x, y, z, value):
        key = (x, y, z)
        self.data[key] = value

    def get(self, x, y, z):
        key = (x, y, z)
        if key in self.data:
            return self.data[key]
        return 0.0

    def set_scale(self, factor):
        self.scale_factor = factor

    def get_scaled_position(self, x, y, z):
        scaled_x = int(math.floor(x / self.scale_factor))
        scaled_y = int(math.floor(y / self.scale_factor))
        scaled_z = int(math.floor(z / self.scale_factor))
        return (scaled_x, scaled_y, scaled_z)

    def get_scaled_value(self, x, y, z):
        pos = self.get_scaled_position(x, y, z)
        return self.get(*pos)

    def get_range_sum(self, min_x, max_x, min_y, max_y, min_z, max_z):
        total = 0.0
        step = self.scale_factor
        if step == 0:
            step = 1.0
        start_x = int(math.floor(min_x / step))
        end_x = int(math.floor(max_x / step)) + 1
        start_y = int(math.floor(min_y / step))
        end_y = int(math.floor(max_y / step)) + 1
        start_z = int(math.floor(min_z / step))
        end_z = int(math.floor(max_z / step)) + 1
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                for z in range(start_z, end_z):
                    if (x, y, z) in self.data:
                        val = self.data[x, y, z]
                        cell_min_x = x * self.scale_factor
                        cell_max_x = (x + 1) * self.scale_factor
                        cell_min_y = y * self.scale_factor
                        cell_max_y = (y + 1) * self.scale_factor
                        cell_min_z = z * self.scale_factor
                        cell_max_z = (z + 1) * self.scale_factor
                        if not (cell_max_x <= min_x or cell_min_x >= max_x or cell_max_y <= min_y or (cell_min_y >= max_y) or (cell_max_z <= min_z) or (cell_min_z >= max_z)):
                            total += val
        return total
if __name__ == '__main__':
    volume = SparseVolume()
    volume.set(0, 0, 0, 10.0)
    volume.set(1, 1, 1, 20.0)
    volume.set(10, 10, 10, 5.0)
    volume.set_scale(10.0)
    val_at_5_5_5 = volume.get_scaled_value(5, 5, 5)
    print(val_at_5_5_5)
    total_in_range = volume.get_range_sum(0, 15, 0, 15, 0, 15)
    print(total_in_range)