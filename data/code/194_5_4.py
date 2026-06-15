def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            if not words:
                return None
            longest_word = ""
            max_length = 0
            for word in words:
                if len(word) > max_length:
                    max_length = len(word)
                    longest_word = word
            return longest_word
    except FileNotFoundError:
        return None
if __name__ == '__main__':
    sample_filename = "words.txt"
    sample_content = "apple banana programming algorithm supercalifragilisticexpialid"
    with open(sample_filename, 'w') as f:
        f.write(sample_content)
    longest = find_longest_word(sample_filename)
    if longest:
        print(longest)