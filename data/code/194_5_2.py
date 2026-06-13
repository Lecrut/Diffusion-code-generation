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
        return "Error: File not found"
    except Exception as e:
        return f"An error occurred: {e}"
if __name__ == '__main__':
    sample_filename = "words.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("apple banana programming algorithm supercalifragilisticexpialid")
        result = find_longest_word(sample_filename)
        print(result)
    except Exception as e:
        print(f"Setup error: {e}")