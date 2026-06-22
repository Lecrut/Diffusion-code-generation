from math import pi

class PrismGeometry:
    VARIANTS = {
        "cube": (16, 5),
        "cylinder": (pi, 10),
        "octahedron": (8.485, 3)
    }

    @staticmethod
    def calculate(base_area, height):
        return base_area * height

def main():
    results = []
    for shape, values in PrismGeometry.VARIANTS.items():
        area, h = values
        volume = PrismGeometry.calculate(area, h)
        results.append((shape, volume))
    
    for name, vol in results:
        print(f"{name}: {vol}")

if __name__ == '__main__':
    main()