import random

def generate_sorted_words(num_words):
    words = [random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(num_words)]
    return sorted(words)

if __name__ == '__main__':
    sample_words = generate_sorted_words(10)
    print(sample_words)