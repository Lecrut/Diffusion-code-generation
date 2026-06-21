from collections import Counter

class StoreWordCounter:
    def count_top_words(self, descriptions):
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        return word_counts.most_common(5)

if __name__ == '__main__':
    counter = StoreWordCounter()
    descriptions = [
        "Apple store sells apples and oranges",
        "Banana store has bananas and grapes",
        "Apple store offers a variety of fruits"
    ]
    top_words = counter.count_top_words(descriptions)
    for word, count in top_words:
        print(f"{word}: {count}")