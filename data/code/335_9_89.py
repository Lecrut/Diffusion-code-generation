text = "Hello World Python Programming"
words_list = text.split()
print(words_list)
if __name__ == '__main__':
    words_set = set(text.split())
    print(f"Unique count: {len(words_set)}")
    sorted_words = sorted(words_list, key=len)
    print("Shortest to longest:", sorted_words[:3])