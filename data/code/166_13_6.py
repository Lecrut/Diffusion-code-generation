from collections import Counter
SAMPLE_COLORS = ['red', 'blue', 'green', 'red', 'blue', 'red']

def count_color_frequency(colors):
    color_count = Counter(colors)
    sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_colors
if __name__ == '__main__':
    result = count_color_frequency(SAMPLE_COLORS)
    print(result)