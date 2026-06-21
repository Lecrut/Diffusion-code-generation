from collections import Counter

class WordCounter:
    def count_top_words(self, stores):
        descriptions = [
            "Apple store sells apples and oranges",
            "Banana store has bananas and grapes",
            "Apple store has more apples than oranges",
            "Grapes are popular in the Banana store"
        ]
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_words = word_counts.most_common(5)
        return top_words

if __name__ == '__main__':
    counter = WordCounter()
    stores = []
    print(counter.count_top_words(stores))