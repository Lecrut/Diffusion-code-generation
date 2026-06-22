import random

def generate_and_sort_words(num_words):
    words = [random.choice('abcdefghijklmnopqrstuvwxyz') * random.randint(3, 6) for _ in range(num_words)]
    return sorted(words)

if __name__ == '__main__':
    sample_words = generate_and_sort_words(10)
    print(sample_words)