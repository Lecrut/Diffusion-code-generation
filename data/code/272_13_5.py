if __name__ == '__main__':
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    try:
        word_list = [item for item in words if isinstance(item, str)]
        word_list.sort()
        print("Original list of words:", words)
        print("Sorted list of words:", word_list)
    except Exception as e:
        print(f"An error occurred during processing: {e}")