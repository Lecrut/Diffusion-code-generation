class NameCleaner:
    SEPARATOR = ','

    @staticmethod
    def clean_names(names_str):
        return [name.strip() for name in names_str.split(NameCleaner.SEPARATOR)]

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    cleaned_names = NameCleaner.clean_names(sample_input)
    print(cleaned_names)