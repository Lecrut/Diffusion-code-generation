class NameProcessor:
    DELIMITER = ','

    @staticmethod
    def strip_names(names_str):
        return [name.strip() for name in names_str.split(NameProcessor.DELIMITER)]

if __name__ == '__main__':
    sample_names = "  Mike, Nancy ,Oscar, Paul   "
    result = NameProcessor.strip_names(sample_names)
    print(result)