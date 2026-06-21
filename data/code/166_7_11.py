def filter_colors(colors):
    if not all(isinstance(color, str) for color in colors):
        raise ValueError("All elements in the list must be strings")
    
    return [color for color in colors if color.startswith('B')]

if __name__ == '__main__':
    sample_colors = [
        "Blue",
        "Red",
        "Beige",
        "Black",
        "Green"
    ]
    filtered_colors = filter_colors(sample_colors)
    print(filtered_colors)