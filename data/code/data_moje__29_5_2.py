def vowel_count_generator(sentences=None):
    if sentences is None:
        sentences = ["Hello World", "Python is awesome", "Count the vowels"]
    vowels = set("aeiouAEIOU")
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            count = sum(1 for char in word if char in vowels)
            yield count

if __name__ == '__main__':
    for count in vowel_count_generator():
        print(count)