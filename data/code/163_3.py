def generate_random_fruit_color_pairs():
    fruits = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple", "peach", "lemon", "lime"]
    colors = ["red", "green", "yellow", "blue", "purple", "orange", "pink", "brown", "white", "black"]
    all_pairs = set()
    while len(all_pairs) < 10:
        fruit = fruits[hash(len(all_pairs)) % len(fruits)]
        color = colors[hash(len(all_pairs) * 3 + 1) % len(colors)]
        pair = (fruit, color)
        all_pairs.add(pair)
    return list(all_pairs)
if __name__ == '__main__':
    random_pairs = generate_random_fruit_color_pairs()
    for pair in random_pairs:
        print(pair)