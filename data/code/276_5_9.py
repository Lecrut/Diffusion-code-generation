class DictionaryRepeater:
    def __init__(self, repetitions):
        self.repetitions = repetitions

    def repeat_and_merge(self, dictionary):
        result = {}
        for key, value in dictionary.items():
            repeated_value = [value] * self.repetitions
            result[key] = repeated_value
        return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repetitions = 3
    repeater = DictionaryRepeater(repetitions)
    merged_dict = repeater.repeat_and_merge(sample_dict)
    print(merged_dict)