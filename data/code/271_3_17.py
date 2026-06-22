def find_unique_substrings(input_string):
    substrings = set()
    n = len(input_string)
    for i in range(n):
        for j in range(i + 3, n + 1):
            substrings.add(input_string[i:j])
    return substrings

class SubstringFinder:
    def __init__(self, input_string):
        self.input_string = input_string
        self.substrings = find_unique_substrings(input_string)

    def get_substrings(self):
        return sorted(list(self.substrings))

if __name__ == '__main__':
    finder = SubstringFinder("abcde")
    print(finder.get_substrings())