from collections import Counter

def count_color_frequency():
    colors = ["red", "blue", "green", "red", "blue", "red"]
    color_count = Counter(colors)
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors

if __name__ == '__main__':
    result = count_color_frequency()
    print(result)