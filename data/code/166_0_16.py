from typing import List

class ColorTracker:
    DEFAULT_FAVORITES = ["red", "blue"]

    def __init__(self):
        self.favorites: List[str] = ColorTracker.DEFAULT_FAVORITES.copy()

    @staticmethod
    def is_valid_color(color: str) -> bool:
        return isinstance(color, str)

    def add_color(self, color: str) -> None:
        if not self.is_valid_color(color):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            print(f"{color} is already a favorite.")
        else:
            self.favorites.append(color)
            print(f"Added {color} as a favorite.")

    def remove_color(self, color: str) -> None:
        if not self.is_valid_color(color):
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
    tracker.add_color("green")
    tracker.remove_color("blue")
    print(tracker.get_favorites())