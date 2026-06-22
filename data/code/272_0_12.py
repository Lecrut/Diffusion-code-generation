def sort_words(words):
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["strawberry", "blueberry", "raspberry", "blackberry"]
    sorted_list = sort_words(sample_words)
    print(*sorted_list)