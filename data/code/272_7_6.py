import random

def generate_and_sort_words(num_words):
    words = [f"word{i}" for i in range(1, num_words + 1)]
    random.shuffle(words)
    return sorted(words)

if __name__ == '__main__':
    sorted_words = generate_and_sort_words(5)
    print(sorted_words)