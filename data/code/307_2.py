class StringRepeater:
    def repeat(self, text, count):
        return text * count
if __name__ == '__main__':
    repeater = StringRepeater()
    text_to_repeat = "hello"
    number_of_repeats = 3
    result = repeater.repeat(text_to_repeat, number_of_repeats)
    print(result)