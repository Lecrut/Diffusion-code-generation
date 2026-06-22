class StringCleaner:
    @staticmethod
    def remove_spaces(input_list):
        return [item.replace(" ", "") for item in input_list]

if __name__ == '__main__':
    sample_values = ["Hello World", "Python Programming", "Remove Spaces"]
    result = StringCleaner.remove_spaces(sample_values)
    print(result)