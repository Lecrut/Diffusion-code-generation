class SubstringGenerator:
    @staticmethod
    def generate_substrings(s):
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield s[i:j]

if __name__ == '__main__':
    sample_string = "xyz"
    generator_instance = SubstringGenerator()
    all_substrings = list(generator_instance.generate_substrings(sample_string))
    print(all_substrings)