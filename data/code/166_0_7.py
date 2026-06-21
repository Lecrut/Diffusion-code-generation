from typing import List

class ColorTracker:

    def __init__(self):
        self.favorites: List[str] = []

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
    tracker.add_color('blue')
    tracker.add_color('green')
    print(tracker.get_favorites())
    tracker.remove_color('blue')
    print(tracker.get_favorites())