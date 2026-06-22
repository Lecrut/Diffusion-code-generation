import random

def generate_random_words(count):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return [random.choice(words) for _ in range(count)]

def alphabetical_sort(string_iterable):
    return sorted(list(string_iterable))

if __name__ == '__main__':
    random_words = generate_random_words(5)
    print(f"Random Words: {random_words}")
    sorted_words = alphabetical_sort(random_words)
    print(f"Sorted Words: {sorted_words}")