colors = ['Blue', 'Green', 'Black', 'White', 'Brown']

def filter_colors(colors):
    return [color for color in colors if color.startswith('B')]

if __name__ == '__main__':
    filtered_colors = filter_colors(colors)
    print(filtered_colors)