from collections import Counter

class WordCounter:
    def count_top_words(self, descriptions):
        word_counts = Counter(word for desc in descriptions for word in desc.split())
        top_words = word_counts.most_common(5)
        return top_words

if __name__ == '__main__':
    counter = WordCounter()
    descriptions = [
        "Apple store has a variety of fruits",
        "Banana store sells fresh bananas",
        "Apple store offers organic apples",
        "Orange store provides citrus fruits"
    ]
    print(counter.count_top_words(descriptions))