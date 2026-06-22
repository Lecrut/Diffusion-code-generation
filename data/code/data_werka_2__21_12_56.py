STRING_LENGTH_THRESHOLD = 10

def sort_strings_by_length(strings):
    if not strings:
        return []
    return sorted(strings, key=len)

class StringSorter:
    def __init__(self, strings):
        self.strings = strings

    def sort(self):
        return sort_strings_by_length(self.strings)

if __name__ == '__main__':
    sample_values = ["strawberry", "blueberry", "raspberry", "blackberry", "a"]
    sorter = StringSorter(sample_values)
    sorted_values = sorter.sort()
    print(sorted_values)