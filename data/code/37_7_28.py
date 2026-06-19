class StringCombiner:
    SEPARATOR = " "

    @staticmethod
    def combine(str1, str2):
        return str1 + StringCombiner.SEPARATOR + str2

if __name__ == '__main__':
    sample_string_a = "Hello"
    sample_string_b = "World"
    combined_result = StringCombiner.combine(sample_string_a, sample_string_b)
    print(combined_result)