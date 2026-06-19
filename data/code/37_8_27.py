class StringCombiner:

    def __init__(self):
        self.combined_results = []

    def combine_strings(self, str1, str2):
        combined = str1 + str2
        self.combined_results.append(combined)
        return combined
if __name__ == '__main__':
    combiner = StringCombiner()
    string_a = 'Hello'
    string_b = 'World'
    result1 = combiner.combine_strings(string_a, string_b)
    print(f'Combined (A then B): {result1}')
    string_c = 'Python'
    string_d = 'Programming'
    result2 = combiner.combine_strings(string_c, string_d)
    print(f'Combined (C then D): {result2}')
    print('All Combined Results:')
    for idx, res in enumerate(combiner.combined_results):
        print(f'Result {idx + 1}: {res}')