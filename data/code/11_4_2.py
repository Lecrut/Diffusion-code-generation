def find_duplicates(s):
    counts = {}
    for char in s.lower():
        if char.isalpha() or char.isdigit():
            counts[char] = counts.get(char, 0) + 1
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_string = "Programming in Python is Fun!!"
    result = find_duplicates(sample_string)
    print(result)