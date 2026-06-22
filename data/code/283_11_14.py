class StringEnsurer:
    @staticmethod
    def ensure_strings(lst):
        return [str(item) for item in lst]

if __name__ == '__main__':
    sample_list = ['apple', 3.14, True, None]
    result = StringEnsurer.ensure_strings(sample_list)
    print(result)