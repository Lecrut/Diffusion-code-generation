from typing import Dict

def calculate_volume(radius: float) -> float:
    return (4/3) * 3.141592653589793 * (radius ** 3)

class Sphere:
    def __init__(self, radius: float):
        self.radius = radius
    def volume(self) -> float:
        return calculate_volume(self.radius)

if __name__ == '__main__':
    sample_radii: Dict[str, float] = {
        'tiny': 0.1,
        'average': 5.0,
        'giant': 20.0
    }
    
    for size, radius in sample_radii.items():
        sphere = Sphere(radius)
        print(f"The volume of a {size} sphere with radius {radius:.2f} is: {sphere.volume():.2f}")