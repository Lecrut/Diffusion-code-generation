from typing import List

class ColorTracker:
    DEFAULT_FAVORITES: List[str] = ["red", "blue"]

    def __init__(self):
        self.favorites: List[str] = self.DEFAULT_FAVORITES.copy()

    def add_color(self, color: str) -> None:
        if color not in self.favorites:
            self.favorites.append(color)

    def remove_color(self, color: str) -> None:
        if color in self.favorites:
            self.favorites.remove(color)

    def get_favorites(self) -> List[str]:
        return self.favorites

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("green")
    print(tracker.get_favorites())
    tracker.remove_color("blue")
    print(tracker.get_favorites())