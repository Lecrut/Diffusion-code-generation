class StringManipulator:
    def remove_spaces(self, input_string):
        return input_string.replace(' ', '')

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string1 = '  Hello World!  '
    sample_string2 = 'Python programming is fun.'
    
    result1 = manipulator.remove_spaces(sample_string1)
    result2 = manipulator.remove_spaces(sample_string2)
    
    print(result1)
    print(result2)