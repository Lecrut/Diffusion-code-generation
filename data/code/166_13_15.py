from collections import Counter

def count_color_frequency(colors):
    return sorted(Counter(colors).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_colors = ['red', 'blue', 'green', 'red', 'blue', 'red']
    result = count_color_frequency(sample_colors)
    print(result)