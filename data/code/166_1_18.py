FAVORITE_COLORS = ["red", "blue", "green", "yellow"]

def initialize_and_sort_colors(colors):
    return sorted(set(colors))

if __name__ == '__main__':
    sample_colors = FAVORITE_COLORS * 2 + ["purple"]
    result = initialize_and_sort_colors(sample_colors)
    print(result)