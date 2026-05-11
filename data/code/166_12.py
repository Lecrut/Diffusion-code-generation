import random
def collect_colors():
    favorite_colors = set()
    sample_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
    for _ in range(5):
        color = random.choice(sample_colors)
        favorite_colors.add(color)
    print("Final favorite colors:", sorted(list(favorite_colors)))
if __name__ == '__main__':
    collect_colors()