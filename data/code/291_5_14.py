class Measure:
    def __init__(self, decimeters: int, centimeters: int):
        self.decimeters = decimeters
        self.centimeters = centimeters

    @property
    def total_centimeters(self) -> int:
        return self.decimeters * 10 + self.centimeters

    def compare_to(self, other: 'Measure') -> str:
        if self.total_centimeters > other.total_centimeters:
            return f"{self.decimeters}dm {self.centimeters}cm"
        else:
            return f"{other.decimeters}dm {other.centimeters}cm"

if __name__ == '__main__':
    measure1 = Measure(3, 5)
    measure2 = Measure(4, 2)
    print(measure1.compare_to(measure2))