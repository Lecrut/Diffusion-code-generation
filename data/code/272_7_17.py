import random

def generate_sorted_words(num_words):
    words = [random.choice('abcdefghijklmnopqrstuvwxyz') * random.randint(3, 6) for _ in range(num_words)]
    words.sort()
    return words

if __name__ == '__main__':
    sorted_words = generate_sorted_words(10)
    print(sorted_words)