from collections import Counter

def count_color_frequencies(colors):
    return sorted(Counter(colors).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 'green', 'red', 'blue', 'red']
    print(count_color_frequencies(sample_colors))