from collections import Counter

class WordCounter:
    def count_top_words(self, descriptions):
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_words = word_counts.most_common(5)
        return top_words

if __name__ == '__main__':
    counter = WordCounter()
    sample_descriptions = [
        "Apple store sells apples and oranges",
        "Banana store has bananas and grapes",
        "Apple store has more apples than oranges",
        "Grapes are popular in the Banana store"
    ]
    top_words = counter.count_top_words(sample_descriptions)
    print(top_words)