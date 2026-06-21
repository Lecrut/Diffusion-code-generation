from collections import Counter

class WordCounter:
    def count_top_words(self, descriptions):
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_words = word_counts.most_common(5)
        return top_words

if __name__ == '__main__':
    counter = WordCounter()
    descriptions = [
        "Apple store sells apples oranges bananas",
        "Banana store has lots of bananas",
        "Orange store is famous for oranges",
        "Apple store also sells oranges"
    ]
    print(counter.count_top_words(descriptions))