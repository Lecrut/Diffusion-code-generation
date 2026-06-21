class NameCleaner:
    DELIMITER = ','

    @staticmethod
    def clean_names(names_str):
        return [name.strip() for name in names_str.split(NameCleaner.DELIMITER)]

if __name__ == '__main__':
    sample_input = "Alice, Bob , Charlie ,David"
    result = NameCleaner.clean_names(sample_input)
    print(result)