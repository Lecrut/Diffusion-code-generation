import random

def generate_random_words(num_words):
    return [random.choice("abcdefghijklmnopqrstuvwxyz") * 5 for _ in range(num_words)]

def alphabetical_sort(words_list):
    return sorted(words_list)

if __name__ == '__main__':
    try:
        sample1 = generate_random_words(4)
        result1 = alphabetical_sort(sample1)
        print(f"Sample 1 Input: {sample1}")
        print(f"Sample 1 Output: {result1}")

        sample2 = generate_random_words(5)
        result2 = alphabetical_sort(sample2)
        print(f"Sample 2 Input: {sample2}")
        print(f"Sample 2 Output: {result2}")

        sample3 = generate_random_words(6)
        result3 = alphabetical_sort(sample3)
        print(f"Sample 3 Input: {sample3}")
        print(f"Sample 3 Output: {result3}")

    except Exception as e:
        print(f"An error occurred: {e}")