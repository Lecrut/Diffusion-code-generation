from typing import List

class ColorTracker:
    def __init__(self):
        self.favorites: List[str] = []

    def add_favorite(self, color: str) -> None:
        if color not in self.favorites:
            self.favorites.append(color)

    def remove_favorite(self, color: str) -> None:
        if color in self.favorites:
            self.favorites.remove(color)

    def get_favorites(self) -> List[str]:
        return self.favorites

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_favorite('red')
    tracker.add_favorite('blue')
    print(tracker.get_favorites())
    tracker.remove_favorite('red')
    print(tracker.get_favorites())