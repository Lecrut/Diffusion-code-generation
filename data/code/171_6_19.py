from collections import Counter

class StoreWordCounter:
    def __init__(self):
        self.descriptions = [
            "Apple store sells apples and oranges",
            "Banana store has bananas and grapes",
            "Apple store has more apples than oranges",
            "Grapes are popular in the Banana store"
        ]

    def count_top_words(self, stores):
        descriptions = [desc for store in stores for desc in self.descriptions if store.lower() in desc.lower()]
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_5_words = word_counts.most_common(5)
        return top_5_words

if __name__ == '__main__':
    counter = StoreWordCounter()
    stores = ["Apple store", "Banana store"]
    result = counter.count_top_words(stores)
    print(result)