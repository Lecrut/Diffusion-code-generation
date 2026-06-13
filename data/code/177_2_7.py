import re
def split_and_filter(text):
    words = re.split(r'\s+', text)
    filtered_words = [word for word in words if word]
    return filtered_words
if __name__ == '__main__':
    sample1 = "  hello   world  this is a test "
    sample2 = "multiple   spaces\tand\ttabs"
    sample3 = " leading and trailing spaces "
    sample4 = "   "
    sample5 = ""
    print(f"Sample 1: {split_and_filter(sample1)}")
    print(f"Sample 2: {split_and_filter(sample2)}")
    print(f"Sample 3: {split_and_filter(sample3)}")
    print(f"Sample 4: {split_and_filter(sample4)}")
    print(f"Sample 5: {split_and_filter(sample5)}")