from collections import Counter

class WordCounter:
    def count_top_words(self, descriptions):
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_5_words = word_counts.most_common(5)
        return top_5_words

if __name__ == '__main__':
    counter = WordCounter()
    descriptions = [
        "Apple store sells apples and oranges",
        "Banana store has bananas and grapes",
        "Apple store offers a variety of fruits"
    ]
    print(counter.count_top_words(descriptions))