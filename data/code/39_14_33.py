class SubstringGenerator:
    @staticmethod
    def generate_substrings(s):
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                yield s[i:j+1]

if __name__ == '__main__':
    sample_string = "abc"
    generator_instance = SubstringGenerator()
    all_substrings = list(generator_instance.generate_substrings(sample_string))
    print(all_substrings)