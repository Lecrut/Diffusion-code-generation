from collections import Counter

def calculate_color_frequency(colors):
    if not all(isinstance(color, str) for color in colors):
        raise ValueError("All elements must be strings")
    
    return dict(Counter(colors))

if __name__ == '__main__':
    favorite_colors = ["red", "blue", "green", "yellow", "purple", "orange", "red"]
    frequency = calculate_color_frequency(favorite_colors)
    print(frequency)