from typing import List

class ColorTracker:
    def __init__(self):
        self.favorites: List[str] = []

    def add_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            raise ValueError(f"{color} is already a favorite.")
        self.favorites.append(color)

    def remove_color(self, color: str) -> None:
        if not isinstance(color, str):
            raise ValueError("Invalid input. Please provide a string.")
        if color in self.favorites:
            self.favorites.remove(color)
        else:
            raise ValueError(f"{color} is not a favorite.")

    def get_favorites(self) -> List[str]:
        return self.favorites.copy()

if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color("red")
    tracker.add_color("blue")
    print(tracker.get_favorites())
    try:
        tracker.remove_color("green")
    except ValueError as e:
        print(e)
    tracker.remove_color("blue")
    print(tracker.get_favorites())