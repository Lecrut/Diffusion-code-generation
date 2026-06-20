class DataCleaner:
    NUMERIC_TYPES = (int, float)
    STR_TO_NUM_MAP = str.maketrans('.,', '  ')

    @staticmethod
    def is_valid_number(value: str) -> bool:
        value = value.translate(DataCleaner.STR_TO_NUM_MAP).strip()
        return value.replace('.', '', 1).isdigit()

    @classmethod
    def clean_and_convert(cls, data):
        cleaned_data = []
        for item in data:
            if isinstance(item, cls.NUMERIC_TYPES):
                cleaned_data.append(item)
            elif isinstance(item, str) and cls.is_valid_number(item):
                cleaned_data.append(int(item) if '.' not in item else float(item))
        return cleaned_data

if __name__ == '__main__':
    sample_data = [1, '2', 3.0, None, '4.5', 'abc']
    cleaner = DataCleaner()
    print(cleaner.clean_and_convert(sample_data))