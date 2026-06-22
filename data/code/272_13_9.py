def sort_words(words):
    if not all(isinstance(item, str) for item in words):
        raise ValueError("All elements in the list must be strings.")
    return sorted(words)

if __name__ == '__main__':
    try:
        sample_words = ["banana", "apple", "cherry"]
        print(sort_words(sample_words))
    except ValueError as e:
        print(f"Error: {e}")