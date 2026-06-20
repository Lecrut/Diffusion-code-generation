class VowelStripper:
    VOWELS = set('aeiouAEIOU')

    @staticmethod
    def strip(text):
        return ''.join([c for c in text if c not in VowelStripper.VOWELS])

if __name__ == '__main__':
    sample = "Python is awesome"
    print(VowelStripper.strip(sample))