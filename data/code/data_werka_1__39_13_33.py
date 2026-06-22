class SubstringExtractor:

    def __init__(self, s):
        self.s = s

    def extract(self, start, end):
        start_indices = [i for i, char in enumerate(self.s) if char == start]
        end_indices = [j for j, char in enumerate(self.s) if char == end]
        return [self.s[i:j + 1] for i in start_indices for j in end_indices if i < j]
if __name__ == '__main__':
    target_string = 'abcdeabc'
    extractor = SubstringExtractor(target_string)
    start_point = 'a'
    end_point = 'e'
    result = extractor.extract(start_point, end_point)
    print(result)
    another_target = 'xyzzyx'
    another_extractor = SubstringExtractor(another_target)
    print(another_extractor.extract('x', 'y'))
    print(another_extractor.extract('z', 'x'))