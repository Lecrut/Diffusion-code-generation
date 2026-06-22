class PrefixValidator:
    def __init__(self, first_chars):
        self.allowed_starts = tuple(first_chars)

    def has_match(self, word_list):
        for word in word_list:
            if word and word[0] in self.allowed_starts:
                return True
        return False

if __name__ == '__main__':
    validator = PrefixValidator(['A', 'B'])
    list_one = ['Aardvark', 'Zebra']
    list_two = ['Monkey', 'Giraffe']
    
    print(validator.has_match(list_one))
    print(validator.has_match(list_two))