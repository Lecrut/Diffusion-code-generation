class FavoriteColors:
    def __init__(self):
        self.colors = {"red", "blue", "green", "yellow", "purple"}

    def has_color(self, color):
        return color in self.colors

if __name__ == '__main__':
    favorite_colors = FavoriteColors()
    sample_colors = ["red", "orange", "green"]
    
    for color in sample_colors:
        print(f"Checking if '{color}' is a favorite color: {favorite_colors.has_color(color)}")