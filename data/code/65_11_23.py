class StringPrinter:
    INDEX_FORMAT = "{}: {}"

    @staticmethod
    def print_strings_with_index(strings):
        for index, string in enumerate(strings):
            print(StringPrinter.INDEX_FORMAT.format(index, string))

if __name__ == '__main__':
    sample_values = ["grape", "melon", "kiwi", "mango"]
    StringPrinter.print_strings_with_index(sample_values)