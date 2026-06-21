from collections import Counter

COLORS = [
    "red", "blue", "green", "red",
    "blue", "red", "yellow", "orange",
    "red", "violet", "indigo", "blue"
]

def count_color_frequency():
    color_count = Counter(COLORS)
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors

if __name__ == '__main__':
    result = count_color_frequency()
    print(result)