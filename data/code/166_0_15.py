from typing import List

FAVORITE_COLOR_PREFIX = "favorite"

class ColorTracker:
    def __init__(self):
        self.favorites: List[str] = []

    def add_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise ValueError("Invalid input. Please provide a string.")
        if FAVORITE_COLOR_PREFIX in color:
            print(f"{color} is already a favorite.")
        else:
            self.favorites.append(FAVORITE_COLOR_PREFIX + color)
            print(f"Added {color} as a favorite.")

    def remove_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise ValueError("Invalid input. Please provide a string.")
        if FAVORITE_COLOR_PREFIX in color:
            self.favorites.remove(color)
            print(f"Removed {color} from favorites.")

    def get_favorites(self) -> List[str]:
        return [color.replace(FAVORITE_COLOR_PREFIX, '') for color in self.favorites]

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("red")
    tracker.add_color("blue")
    print(tracker.get_favorites())
    tracker.remove_color("red")