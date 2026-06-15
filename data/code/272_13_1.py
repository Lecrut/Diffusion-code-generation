if __name__ == '__main__':
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    try:
        word_list = []
        for item in words:
            if isinstance(item, str):
                word_list.append(item)
            else:
                print(f"Skipping invalid input: {item}")
        word_list.sort()
        print("Original list of words:", words)
        print("Sorted list of words:", word_list)
    except Exception as e:
        print(f"An error occurred: {e}")