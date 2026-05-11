import time
def track_favorite_colors(color_list):
    unique_colors = set(color_list)
    sorted_colors = sorted(list(unique_colors))
    return sorted_colors
if __name__ == '__main__':
    sample_colors = ["red", "blue", "green", "red", "yellow", "blue", "red", "purple"]
    start_time = time.time()
    favorite_colors = track_favorite_colors(sample_colors)
    end_time = time.time()
    print(favorite_colors)