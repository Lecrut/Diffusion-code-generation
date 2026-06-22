class StringRepeater:
    SEQUENCE = 'AB'
    
    @staticmethod
    def repeat_sequence(sequence, n):
        return sequence * n
    
    @classmethod
    def generate_string(cls, repetitions=1000):
        return cls.repeat_sequence(cls.SEQUENCE, repetitions)

if __name__ == '__main__':
    result = StringRepeater.generate_string()
    print(result)