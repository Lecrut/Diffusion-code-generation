class StringRepeater:
    PATTERN = 'AB'
    
    @staticmethod
    def repeat_pattern(n):
        return StringRepeater.PATTERN * n

if __name__ == '__main__':
    repetitions = 1000
    result = StringRepeater.repeat_pattern(repetitions)
    print(result)