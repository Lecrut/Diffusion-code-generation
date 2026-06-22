class StringManipulator:
    def remove_spaces(self, input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    manipulator = StringManipulator()
    test_string1 = "hello world"
    result1 = manipulator.remove_spaces(test_string1)
    print(result1)
    test_string2 = "   this has spaces   "
    result2 = manipulator.remove_spaces(test_string2)
    print(result2)
    test_string3 = "no_spaces"
    result3 = manipulator.remove_spaces(test_string3)
    print(result3)