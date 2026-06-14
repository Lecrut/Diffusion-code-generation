class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def calculate_volume(self):
        return self.length * self.width * self.height
    def calculate_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
if __name__ == '__main__':
    box1 = Box(10, 5, 3)
    print(f"Box 1 Volume: {box1.calculate_volume()}")
    print(f"Box 1 Surface Area: {box1.calculate_surface_area()}")
    box2 = Box(4, 6, 2)
    print(f"Box 2 Volume: {box2.calculate_volume()}")
    print(f"Box 2 Surface Area: {box2.calculate_surface_area()}")