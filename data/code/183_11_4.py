class NameParser:
    DELIMITER = ';'
    
    @staticmethod
    def clean_names(names):
        return [name.strip() for name in names if name.strip()]
    
    @classmethod
    def parse_line(cls, line):
        return cls.clean_names(line.split(cls.DELIMITER))

if __name__ == '__main__':
    sample_line = "Zoe; Alex ; Casey;; Dana"
    print(NameParser.parse_line(sample_line))