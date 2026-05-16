class StringCapitalizer:
    def capitalize_words(self, text):
        words = text.split()
        capitalized_words = []
        for word in words:
            if word:
                capitalized_words.append(word.capitalize())
            else:
                capitalized_words.append(word)
        return " ".join(capitalized_words)
if __name__ == '__main__':
    capitalizer = StringCapitalizer()
    sample_string1 = "hello world this is a test"
    sample_string2 = "this is a sample string for capitalization"
    sample_string3 = "a short sentence"
    print(f"Original: '{sample_string1}'")
    print(f"Capitalized: '{capitalizer.capitalize_words(sample_string1)}'")
    print("-" * 20)
    print(f"Original: '{sample_string2}'")
    print(f"Capitalized: '{capitalizer.capitalize_words(sample_string2)}'")
    print("-" * 20)
    print(f"Original: '{sample_string3}'")
    print(f"Capitalized: '{capitalizer.capitalize_words(sample_string3)}'")