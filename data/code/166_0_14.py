from typing import List

class ColorTracker:
    DEFAULT_FAVORITE_COLORS = ["red", "blue"]

    def __init__(self):
        self.favorites: List[str] = []

    @staticmethod
    def _is_valid_color(color: str) -> bool:
        return isinstance(color, str)

    def add_color(self, color: str) -> None:
        if not ColorTracker._is_valid_color(color):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            print(f"{color} is already a favorite.")
        else:
            self.favorites.append(color)
            print(f"Added {color} as a favorite.")

    def remove_color(self, color: str) -> None:
        if not ColorTracker._is_valid_color(color):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            self.favorites.remove(color)
            print(f"Removed {color} from favorites.")
        else:
            print(f"{color} is not a favorite.")

    def get_favorites(self) -> List[str]:
        return self.favorites

if __name__ == '__main__':
    tracker = ColorTracker()
    for color in ColorTracker.DEFAULT_FAVORITE_COLORS:
        tracker.add_color(color)
    print(tracker.get_favorites())
    tracker.remove_color("red")
    print(tracker.get_favorites())