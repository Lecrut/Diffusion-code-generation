from typing import List

class ColorTracker:
    DEFAULT_FAVORITE_COLORS = ["red", "blue"]

    def __init__(self):
        self.favorites: List[str] = self.DEFAULT_FAVORITE_COLORS.copy()

    @staticmethod
    def _is_valid_color(color: str) -> bool:
        return isinstance(color, str)

    def add_color(self, color: str) -> None:
        if not self._is_valid_color(color):
            raise ValueError("Invalid input. Please provide a string.")
        if color not in self.favorites:
            self.favorites.append(color)
            print(f"Added {color} as a favorite.")

    def remove_color(self, color: str) -> None:
        if not self._is_valid_color(color):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            self.favorites.remove(color)
            print(f"Removed {color} from favorites.")

    def get_favorites(self) -> List[str]:
        return self.favorites

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("green")
    print(tracker.get_favorites())
    tracker.remove_color("red")