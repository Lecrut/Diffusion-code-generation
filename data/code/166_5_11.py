def color_frequency_counter():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "red", "blue"]
    counter = {}
    for color in colors:
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 1
    return counter

if __name__ == '__main__':
    frequency_counter = color_frequency_counter()
    print(frequency_counter)