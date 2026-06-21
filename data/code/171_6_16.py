from collections import Counter

class StoreWordCounter:
    def __init__(self, stores):
        self.descriptions = [
            f"{store} sells a variety of fruits" for store in stores
        ]

    def count_top_words(self):
        word_counts = Counter(word for desc in self.descriptions for word in desc.split())
        top_words = word_counts.most_common(5)
        return top_words

if __name__ == '__main__':
    stores = ["Apple store", "Banana store", "Orange store"]
    counter = StoreWordCounter(stores)
    result = counter.count_top_words()
    print(result)