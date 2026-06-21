class NameProcessor:
    SEPARATOR = '|'
    
    @staticmethod
    def clean_names(names_list):
        return [name.strip() for name in names_list if name]
    
    @classmethod
    def extract_and_clean_names(cls, pipe_delimited_string):
        names = pipe_delimited_string.split(cls.SEPARATOR)
        return cls.clean_names(names)

if __name__ == '__main__':
    sample_input = "  Alice | Bob   | Charlie| "
    cleaned_names = NameProcessor.extract_and_clean_names(sample_input)
    print(cleaned_names)