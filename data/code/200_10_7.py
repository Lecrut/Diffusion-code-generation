class StringFilter:
    @staticmethod
    def is_alpha(s):
        return s.isalpha()

    @classmethod
    def filter_strings(cls, string_list):
        return [s for s in string_list if cls.is_alpha(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world!", "Python3", "code"]
    filtered_values = StringFilter.filter_strings(sample_values)
    print(filtered_values)