class LongestItemFinder:
    def __init__(self):
        self.longest_item = ""

    def update_longest(self, item):
        if len(item) > len(self.longest_item):
            self.longest_item = item

    def find_longest(self, string_list):
        for s in string_list:
            self.update_longest(s)
        return self.longest_item

if __name__ == '__main__':
    finder = LongestItemFinder()
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    longest_item = finder.find_longest(sample_list)
    print(longest_item)