class StringEnsurer:
    def __init__(self, data):
        self.data = data

    def ensure_strings(self):
        return [str(item) for item in self.data]

if __name__ == '__main__':
    sample_list = ['apple', 3.14, True, None]
    ensurer = StringEnsurer(sample_list)
    result = ensurer.ensure_strings()
    print(result)