from collections import Counter

def count_color_frequency(colors):
    return sorted(Counter(colors).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    favorite_colors = ['blue', 'red', 'green', 'blue', 'yellow', 'red', 'red']
    print(count_color_frequency(favorite_colors))