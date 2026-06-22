from dataclasses import dataclass

DIMENSION_ONE: float = 10.0
DIMENSION_TWO: float = 5.0
DIMENSION_THREE: float = 3.0
TWO: float = 2.0

@dataclass
class RectangularBox:
    edge_a: float
    edge_b: float
    edge_c: float

    def get_surface_area(self) -> float:
        area_top_bottom: float = self.edge_a * self.edge_b
        area_front_back: float = self.edge_a * self.edge_c
        area_left_right: float = self.edge_b * self.edge_c
        total_area: float = TWO * (area_top_bottom + area_front_back + area_left_right)
        return total_area

if __name__ == '__main__':
    box_dimensions = RectangularBox(
        edge_a=DIMENSION_ONE,
        edge_b=DIMENSION_TWO,
        edge_c=DIMENSION_THREE
    )
    computed_area = box_dimensions.get_surface_area()
    print(computed_area)