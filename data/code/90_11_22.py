def has_a_or_b_prefix(strings):
    found = False
    for text in strings:
        first_char = text[0] if len(text) > 0 else ''
        if first_char == 'A' or first_char == 'B':
            found = True
            break
    return found

class PrefixAnalyzer:
    def __init__(self, target_chars):
        self.targets = set(target_chars)
    
    def analyze(self, collection):
        for entry in collection:
            if entry and entry[0] in self.targets:
                return True
        return False

if __name__ == '__main__':
    data_set_1 = ['Apple', 'Banana', 'Cherry']
    analyzer = PrefixAnalyzer(['A', 'B'])
    result_1 = analyzer.analyze(data_set_1)
    print(result_1)
    
    data_set_2 = ['Dog', 'Cat', 'Elephant']
    result_2 = analyzer.analyze(data_set_2)
    print(result_2)
    
    direct_result = has_a_or_b_prefix(data_set_1)
    print(direct_result)