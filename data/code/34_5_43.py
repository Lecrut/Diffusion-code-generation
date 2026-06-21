class CapitalizeDecorator:
    @staticmethod
    def capitalize_string(text):
        return ' '.join(word.capitalize() for word in text.split())

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return self.capitalize_string(result)

@CapitalizeDecorator
def get_greeting():
    return "hello world"

if __name__ == '__main__':
    sample_text = "this is another test string"
    capitalized_text = get_greeting()
    print("Original:", sample_text)
    print("Capitalized:", capitalized_text)