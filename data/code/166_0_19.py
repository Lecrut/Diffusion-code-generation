from typing import List

FAVORITE_COLOR = "favorite"

class ColorTracker:
    def __init__(self):
        self.favorites: List[str] = []

    def add_color(self, color: str) -> None:
        if color not in self.favorites:
            self.favorites.append(color)
            print(f"Added {color} as a favorite.")
        else:
            print(f"{color} is already a favorite.")

    def remove_color(self, color: str) -> None:
        if color in self.favorites:
            self.favorites.remove(color)
            print(f"Removed {color} from favorites.")
        else:
            print(f"{color} is not a favorite.")

    def get_favorites(self) -> List[str]:
        return self.favorites

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("red")
    tracker.add_color("blue")
    print(tracker.get_favorites())
    tracker.remove_color("red")