def split_and_filter(text):
    parts = text.split(' ')
    filtered_parts = [part for part in parts if part]
    return filtered_parts
if __name__ == '__main__':
    sample1 = "this is a test"
    sample2 = "  leading and trailing spaces "
    sample3 = "multiple   spaces   here"
    sample4 = "singleword"
    sample5 = ""
    sample6 = "word1  word2\tword3"
    print(f"'{sample1}' -> {split_and_filter(sample1)}")
    print(f"'{sample2}' -> {split_and_filter(sample2)}")
    print(f"'{sample3}' -> {split_and_filter(sample3)}")
    print(f"'{sample4}' -> {split_and_filter(sample4)}")
    print(f"'{sample5}' -> {split_and_filter(sample5)}")
    print(f"'{sample6}' -> {split_and_filter(sample6)}")