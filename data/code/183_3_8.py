class NameExtractor:
    SEPARATOR = '|'
    
    @staticmethod
    def extract_names(pipe_delimited_string):
        return pipe_delimited_string.split(NameExtractor.SEPARATOR)

if __name__ == '__main__':
    sample_input = "Zoe|Adam|Beth"
    extractor = NameExtractor()
    names_list = extractor.extract_names(sample_input)
    print(names_list)