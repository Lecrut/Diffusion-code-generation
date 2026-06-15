if __name__ == '__main__':
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    try:
        word_list = []
        for item in words:
            if isinstance(item, str):
                word_list.append(item)
            else:
                print(f"Warning: Skipped non-string input: {item}")
        word_list.sort()
        print("Original list of words (after filtering non-strings):")
        print(word_list)
        print("\nAlphabetically sorted list:")
        for word in word_list:
            print(word)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")