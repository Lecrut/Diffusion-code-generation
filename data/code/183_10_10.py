class NameCleaner:
    def __init__(self, names_str):
        self.names = [name.strip() for name in names_str.split(',')]

    def get_cleaned_names(self):
        return self.names

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    cleaner = NameCleaner(sample_input)
    print(cleaner.get_cleaned_names())