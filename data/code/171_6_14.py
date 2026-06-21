from collections import Counter

class WordCounter:
    def count_top_words(self, descriptions):
        words = ' '.join(descriptions).lower().split()
        word_counts = Counter(words)
        top_5_words = word_counts.most_common(5)
        return top_5_words

if __name__ == '__main__':
    counter = WordCounter()
    descriptions = [
        "Apple store sells apples and oranges",
        "Banana stand has bananas and grapes",
        "Apple store offers a variety of fruits",
        "Grapes are popular in the Banana store"
    ]
    print(counter.count_top_words(descriptions))