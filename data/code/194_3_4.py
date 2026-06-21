class ElementFinder:
    @staticmethod
    def find_longest_element(elements):
        return max(elements, key=len)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    longest_element = ElementFinder.find_longest_element(sample_list)
    print(longest_element)