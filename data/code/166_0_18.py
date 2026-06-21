from typing import List

class ColorTracker:
    DEFAULT_FAVORITE_COLOR = 'blue'

    def __init__(self):
        self.favorites: List[str] = []

    @staticmethod
    def is_valid_color(color: str) -> bool:
        valid_colors = ['red', 'green', 'yellow']
        return color in valid_colors

    def add_color(self, color: str) -> None:
        if not ColorTracker.is_valid_color(color):
            raise ValueError(f'Invalid color: {color}')
        if color not in self.favorites:
            self.favorites.append(color)
            print(f'{color} added as a favorite.')

    def remove_color(self, color: str) -> None:
        if not ColorTracker.is_valid_color(color):
            raise ValueError(f'Invalid color: {color}')
        if color in self.favorites:
            self.favorites.remove(color)
            print(f'{color} removed from favorites.')

    def get_favorites(self) -> List[str]:
        return self.favorites
if __name__ == '__main__':
    tracker = ColorTracker()
    tracker.add_color('red')
    try:
        tracker.add_color('purple')
    except ValueError as e:
        print(e)
    print(tracker.get_favorites())
    tracker.remove_color('red')
    print(tracker.get_favorites())