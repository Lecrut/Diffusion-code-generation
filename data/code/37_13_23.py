class StringMerger:

    def __init__(self, separator):
        self.separator = separator

    def merge(self, str1, str2):
        return f'{str1}{self.separator}{str2}'
if __name__ == '__main__':
    string_a = 'Hello'
    string_b = 'World'
    merger = StringMerger(' and ')
    merged_string = merger.merge(string_a, string_b)
    print(merged_string)
    another_merger = StringMerger('---')
    another_merged_string = another_merger.merge(string_a, string_b)
    print(another_merged_string)