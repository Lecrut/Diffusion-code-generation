import collections

def find_duplicate_chars(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    frequency_map = collections.Counter(text)
    duplicates = {char: count for char, count in frequency_map.items() if count > 1}
    return duplicates

if __name__ == '__main__':
    sample_text = "programming is fun and code has characters that repeat"
    result = find_duplicate_chars(sample_text)
    print(f"Total length of input string: {len(sample_text)}")
    print(f"Number of characters appearing more than once: {len(result)}")
    most_common_duplicate = max(result.items(), key=lambda item: item[1])
    print(f"Most frequent duplicate character: '{most_common_duplicate[0]}' appearing {most_common_duplicate[1]} times")
    if len(result) > 0:
        print("Top 3 most frequent duplicates:", sorted(result.items(), key=lambda item: item[1], reverse=True)[:3])