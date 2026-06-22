class HelloWorldRepeater:
    SEQUENCE = 'Hello World'
    
    @staticmethod
    def repeat_sequence(sequence, repetitions):
        return [sequence] * repetitions
    
if __name__ == '__main__':
    repeater = HelloWorldRepeater()
    repeated_list = repeater.repeat_sequence(HelloWorldRepeater.SEQUENCE, 100)
    result = '\n'.join(repeated_list)
    print(result)