class StringProcessor:

    def __init__(self, text):
        self.text = text

    def apply_rule(self, rule):
        rules = {'title': self._to_title, 'upper': self._to_upper, 'lower': self._to_lower}
        if rule in rules:
            return rules[rule]()
        else:
            raise ValueError('Unsupported capitalization rule')

    def _to_title(self):
        return self.text.title()

    def _to_upper(self):
        return self.text.upper()

    def _to_lower(self):
        return self.text.lower()
if __name__ == '__main__':
    processor = StringProcessor('hello world')
    print(processor.apply_rule('title'))
    print(processor.apply_rule('upper'))
    print(processor.apply_rule('lower'))