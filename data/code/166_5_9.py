colors = ['red', 'blue', 'green', 'blue', 'red', 'yellow']

def calculate_color_frequency(color_list):
    from collections import Counter
    return dict(Counter(color_list))

if __name__ == '__main__':
    frequency = calculate_color_frequency(colors)
    print(frequency)