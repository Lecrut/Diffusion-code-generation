import random
def generate_random_fruit_color_pairs():
    fruits = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple", "peach", "lemon", "lime"]
    colors = ["red", "green", "yellow", "orange", "purple", "blue", "pink", "brown", "white", "black"]
    all_pairs = set()
    while len(all_pairs) < 10:
        fruit = random.choice(fruits)
        color = random.choice(colors)
        all_pairs.add((fruit, color))
    return list(all_pairs)
if __name__ == '__main__':
    random_pairs = generate_random_fruit_color_pairs()
    for pair in random_pairs:
        print(pair)