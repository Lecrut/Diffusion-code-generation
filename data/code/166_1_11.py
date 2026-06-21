favorite_colors = ["red", "blue", "green", "yellow"]

def get_sorted_favorite_colors(colors):
    return sorted(set(colors))

if __name__ == '__main__':
    result = get_sorted_favorite_colors(favorite_colors)
    print(result)