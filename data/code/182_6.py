class StringManipulator:
    def get_all_characters(self, input_string):
        return list(input_string)
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = "Hello World"
    result = manipulator.get_all_characters(sample_string)
    print(result)