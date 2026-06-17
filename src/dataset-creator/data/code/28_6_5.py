from collections import Counter
def find_most_common_animals(animals):
    counter = Counter(animals)
    return counter.most_common()
if __name__ == '__main__':
    sample_data = [
        "cat", "dog", "bird", "fish", "hamster", 
        "cat", "rabbit", "snake", "lizard", "mouse",
        "dog", "cat", "bird", "parrot", "goldfish"
    ]
    result = find_most_common_animals(sample_data)
    for animal, count in result:
        print(f"{animal}: {count}")