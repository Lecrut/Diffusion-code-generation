class StringManipulator:
    def uppercase_string(self, input_string):
        return input_string.upper()
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample1 = "hello world"
    result1 = manipulator.uppercase_string(sample1)
    print(f"Original: {sample1}")
    print(f"Uppercase: {result1}")
    sample2 = "Python Programming"
    result2 = manipulator.uppercase_string(sample2)
    print(f"Original: {sample2}")
    print(f"Uppercase: {result2}")