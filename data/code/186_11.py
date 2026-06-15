import heapq
def order_words(words):
    return sorted(words)
if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_list = order_words(sample_words)
    print(sorted_list)